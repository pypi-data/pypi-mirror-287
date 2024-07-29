class ParseError(Exception):
    """
    Exception raised when user data cannot be correctly parsed.
    """
    
    def __init__(self, flag, arg):
        self.flag = flag
        self.arg = arg
        self.message = f"flag: {self.flag} arg: {self.arg}."
        
    def __str__(self):
        return self.message
        
        
class SyntaxError(Exception):
    """
    Exception raised when there is user input does not match the provided schema.
    
    Examples
    --------
    >>> args = ["helps"]
    >>> new_trait = Trait(args, cmd_dict)
    >>> new_trait.get_result()
    Traceback (most recent call last):
    SyntaxError: Alias 'helps' not found.
    """
    
    def __init__(self, message):
        self.message = f"{message}"
        
    def __str__(self):
        return self.message
        
        
class AssembleError(Exception):
    """
    Exception raised when unable to assemble the final command sequence.
    """
    
    def __init__(self, message):
        self.message = f"{message}"
        
    def __str__(self):
        return self.message
