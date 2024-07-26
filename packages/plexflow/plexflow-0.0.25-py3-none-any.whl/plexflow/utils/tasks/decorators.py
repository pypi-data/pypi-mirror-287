import inspect
from plexflow.core.context.partial_context import PartialContext

def plexflow(task_func):
    def wrapper(*args, **kwargs):
        print("Before task execution")

        # Access the context (ti)
        context = kwargs.get('ti', None)
        context_id = None
        default_ttl = 3600
        if context is not None:
            print("Run ID:", context.run_id)
            print(f"Execution date: {context.execution_date}")
            print(f"Task instance state: {context.state}")
            context_id = context.run_id
        
        sig = inspect.signature(task_func)
        print(sig.parameters)
        
        func_kwargs = {}
        pos_arg_index = 0

        for param_name, param in sig.parameters.items():
            arg_type = param.annotation
            
            if param_name in kwargs:
                func_kwargs[param_name] = kwargs[param_name]
            elif issubclass(arg_type, PartialContext):
                # check if arg_type is subclass of PartialContext
                # Create an instance of the class
                func_kwargs[param_name] = arg_type(context_id=context_id, default_ttl=default_ttl)
            else:
                func_kwargs[param_name] = args[pos_arg_index]
                pos_arg_index += 1
                
        result = task_func(**func_kwargs)

        print("After task execution")
        return result
    return wrapper
