# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/17_callback.tracker.ipynb (unless otherwise specified).

__all__ = ['TerminateOnNaNCallback', 'TrackerCallback', 'EarlyStoppingCallback', 'SaveModelCallback',
           'ReduceLROnPlateau']

# Cell
from ..basics import *
from .progress import *
from .fp16 import MixedPrecision

# Cell
class TerminateOnNaNCallback(Callback):
    "A `Callback` that terminates training if loss is NaN."
    run_before=Recorder

    def after_batch(self):
        "Test if `last_loss` is NaN and interrupts training."
        if torch.isinf(self.loss) or torch.isnan(self.loss): raise CancelFitException

# Cell
class TrackerCallback(Callback):
    "A `Callback` that keeps track of the best value in `monitor`."
    remove_on_fetch,run_after = True,Recorder

    def __init__(self, monitor='valid_loss', comp=None, min_delta=0., reset_on_fit=True):
        if comp is None: comp = np.less if 'loss' in monitor or 'error' in monitor else np.greater
        if comp == np.less: min_delta *= -1
        self.monitor,self.comp,self.min_delta,self.reset_on_fit,self.best= monitor,comp,min_delta,reset_on_fit,None

    def before_fit(self):
        "Prepare the monitored value"
        self.run = not hasattr(self, "lr_finder") and not hasattr(self, "gather_preds")
        if self.reset_on_fit or self.best is None: self.best = float('inf') if self.comp == np.less else -float('inf')
        assert self.monitor in self.recorder.metric_names[1:]
        self.idx = list(self.recorder.metric_names[1:]).index(self.monitor)

    def after_epoch(self):
        "Compare the last value to the best up to now"
        val = self.recorder.values[-1][self.idx]
        if self.comp(val - self.min_delta, self.best): self.best,self.new_best = val,True
        else: self.new_best = False

    def after_fit(self): self.run=True

# Cell
class EarlyStoppingCallback(TrackerCallback):
    "A `TrackerCallback` that terminates training when monitored quantity stops improving."
    def __init__(self, monitor='valid_loss', comp=None, min_delta=0., patience=1, reset_on_fit=True):
        super().__init__(monitor=monitor, comp=comp, min_delta=min_delta, reset_on_fit=reset_on_fit)
        self.patience = patience

    def before_fit(self): self.wait = 0; super().before_fit()
    def after_epoch(self):
        "Compare the value monitored to its best score and maybe stop training."
        super().after_epoch()
        if self.new_best: self.wait = 0
        else:
            self.wait += 1
            if self.wait >= self.patience:
                print(f'No improvement since epoch {self.epoch-self.wait}: early stopping')
                raise CancelFitException()

# Cell
class SaveModelCallback(TrackerCallback):
    "A `TrackerCallback` that saves the model's best during training and loads it at the end."
    _only_train_loop = True
    def __init__(self, monitor='valid_loss', comp=None, min_delta=0., fname='model', every_epoch=False,
                 with_opt=False, reset_on_fit=True):
        super().__init__(monitor=monitor, comp=comp, min_delta=min_delta, reset_on_fit=reset_on_fit)
        # keep track of file path for loggers
        self.last_saved_path = None
        store_attr('fname,every_epoch,with_opt')

    def _save(self, name): self.last_saved_path = self.learn.save(name, with_opt=self.with_opt)

    def after_epoch(self):
        "Compare the value monitored to its best score and save if best."
        if self.every_epoch: self._save(f'{self.fname}_{self.epoch}')
        else: #every improvement
            super().after_epoch()
            if self.new_best:
                print(f'Better model found at epoch {self.epoch} with {self.monitor} value: {self.best}.')
                self._save(f'{self.fname}')

    def after_fit(self, **kwargs):
        "Load the best model."
        if not self.every_epoch: self.learn.load(f'{self.fname}', with_opt=self.with_opt)

# Cell
class ReduceLROnPlateau(TrackerCallback):
    "A `TrackerCallback` that reduces learning rate when a metric has stopped improving."
    def __init__(self, monitor='valid_loss', comp=None, min_delta=0., patience=1, factor=10., min_lr=0, reset_on_fit=True):
        super().__init__(monitor=monitor, comp=comp, min_delta=min_delta, reset_on_fit=reset_on_fit)
        self.patience,self.factor,self.min_lr = patience,factor,min_lr

    def before_fit(self): self.wait = 0; super().before_fit()
    def after_epoch(self):
        "Compare the value monitored to its best score and reduce LR by `factor` if no improvement."
        super().after_epoch()
        if self.new_best: self.wait = 0
        else:
            self.wait += 1
            if self.wait >= self.patience:
                old_lr = self.opt.hypers[-1]['lr']
                for h in self.opt.hypers: h['lr'] = max(h['lr'] / self.factor, self.min_lr)
                self.wait = 0
                if self.opt.hypers[-1]["lr"] < old_lr:
                    print(f'Epoch {self.epoch}: reducing lr to {self.opt.hypers[-1]["lr"]}')