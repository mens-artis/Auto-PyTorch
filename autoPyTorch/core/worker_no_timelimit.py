:
from hpbandster.core.worker import Worker
:

class ModuleWorkerNoTimeLimit(Worker):
    def __init__(self, pipeline, pipeline_config, constant_hyperparameter,
            X_train, Y_train, X_valid, Y_valid, budget_type, max_budget, 
                 working_directory, permutations=None, *args, **kwargs):
        :
        super().__init__(*args, **kwargs)
    
    def compute(self, config, budget, working_directory, config_id, **kwargs):

        config.update(self.constant_hyperparameter)

        if self.guarantee_limits and self.budget_type == 'time':
            import pynisher

            limit_train = pynisher.enforce_limits(mem_in_mb=self.pipeline_config['memory_limit_mb'],
                                           wall_time_in_s=int(budget * 4))(self.optimize_pipeline)
            :
        else:
            result, randomstate = self.optimize_pipeline(config, budget, config_id, 
                                                         random.getstate())

    
    def optimize_pipeline(self, config, budget, config_id, random_state):
        
        :
            
        try:
            self.autonet_logger.info("Fit optimization pipeline")
            return self.pipeline.fit_pipeline(hyperparameter_config=config, 
                                              pipeline_config=self.pipeline_config, 
                                              X_train=self.X_train, Y_train=self.Y_train, 
                                              X_valid=self.X_valid, Y_valid=self.Y_valid, 
                                              budget=budget, budget_type=self.budget_type, 
                                              max_budget=self.max_budget, 
                                              config_id=config_id, 
                                              working_directory=self.working_directory), 
                                              random.getstate()
        :

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True
