import numpy as np
import pandas as pd

from .exceptions import (
    ParseError,
    SyntaxError,
    AssembleError
    )

class Trait():
    """
    Description for class.

    :ivar _params_list: List of arguments for mapping
    :ivar _params_dict: Dictionary for mapping arguements
    :ivar _command_seq: Sequence of commands to return
    """

    def __init__(self, params_list, params_dict):
        """ Assign parameter list and parameter dictionary """

        self._params_list = params_list
        self._params_dict = params_dict
        self._params_set_list = []
        self._command_seq = []
        
        self.PERF_LONG_FLAG = False
        
    def _parse(self, token):

        token_pair = None
        
        try:
            if isinstance(token, list):
                token_pair = token
            else:
                token_pair = [token, None]
        except:
            raise ParseError(token)
        
        return token_pair
    
    def _check_syntax(self, token_pair):
        
        FLAG_ALIAS, FLAG_ARG = token_pair

        # Read the corresponding {syntax_dict}
        SYNTAX_DICT = self._params_dict.get(FLAG_ALIAS, {})

        # Read details for {flag} syntax
        FLAG_LONG = SYNTAX_DICT.get("flag_long", None)
        FLAG_SHRT = SYNTAX_DICT.get("flag_short", None)
        FLAG_REQD = SYNTAX_DICT.get("flag_required", None)
        FLAG_POST = SYNTAX_DICT.get("flag_positional", None)

        # Read details for {arg} syntax
        ARG_REQD = SYNTAX_DICT.get("arg_required", None)
        ARG_TYPE = SYNTAX_DICT.get("arg_type", None)
        ARG_NAME = SYNTAX_DICT.get("arg_name", None)
        ARG_CHOI = SYNTAX_DICT.get("arg_choices", None)

        # Check the {flag} syntax
        if SYNTAX_DICT == {}:
            error_message = f"Alias '{FLAG_ALIAS}' not found."
            raise SyntaxError(error_message)
            return None

        else:

            if self._is_missing_flag(FLAG_LONG, FLAG_SHRT):
                error_message = f"Alias '{FLAG_ALIAS}' missing long_flag and short_flag."
                raise SyntaxError(error_message)
                return None 

            elif self._is_missing_required_arg(ARG_REQD, FLAG_ARG):
                error_message = f"Alias '{FLAG_ALIAS}' requires an argument but none passed."
                raise SyntaxError(error_message)
                return None 
            
            elif self._passed_improper_arg(FLAG_ARG, ARG_NAME):
                error_message = f"Alias '{FLAG_ALIAS}' doesn't accept an argument but was passed '{FLAG_ARG}'."
                raise SyntaxError(error_message)
                return None 

            elif self._is_invalid_arg_choice(FLAG_ARG, ARG_CHOI):
                error_message = f"Alias '{FLAG_ALIAS}' argument '{FLAG_ARG}' must choose from '{ARG_CHOI}'."
                raise SyntaxError(error_message)
                return None 

        FLAG_VALUE = [FLAG for FLAG in [FLAG_LONG, FLAG_SHRT] if FLAG != None]
        
        return [FLAG_VALUE[0], FLAG_ARG]
    

    
    def _assemble(self, sequence):

        try:
            TOKENS = [token for token in sequence if token != None]
            command = " ".join(TOKENS)
        except:
            error_message = f"Unable to process sequence '{sequence}'."
            raise AssembleError(error_message)
            return None
        
        return command
    
    def get_result(self):
        """
        Parse, validate, and return user input as ready to execute command.
        """
    
        command_sequence = []
        
        for param_set in self._params_list:

            token_pair = self._parse(param_set)

            valid_pair = self._check_syntax(token_pair)

            command_sequence.extend(valid_pair)
            
        result = self._assemble(command_sequence)
        return result
    
    # ===========================================================================
    # Error checking functions
    # ---------------------------------------------------------------------------
    def _is_missing_flag(self, FLAG_LONG, FLAG_SHRT):
        """Check for current flag to see if flag_long & flag_short are both None"""

        IS_ERROR = False

        if (FLAG_LONG == None) & (FLAG_SHRT == None):
            IS_ERROR = True

        return IS_ERROR

    def _is_missing_required_arg(self, ARG_REQD, FLAG_ARG):
        """Check to see if an arg is required but was not passed."""

        IS_ERROR = False

        if (ARG_REQD == True) & (FLAG_ARG == None):
            IS_ERROR = True

        return IS_ERROR
    
    def _passed_improper_arg(self, FLAG_ARG, ARG_NAME):
        """Check to see if an arg was passed but the flag doesn't accept an arg."""

        IS_ERROR = False

        if (FLAG_ARG != None) & (ARG_NAME == None):
            IS_ERROR = True

        return IS_ERROR
    
    def _is_invalid_arg_choice(self, FLAG_ARG, ARG_CHOI):
        """Check to see if an arg was passed that did not appear in a list of arg_choices"""

        IS_ERROR = False

        ARG_CHOICE_LIST = self._force_list(ARG_CHOI)

        if (ARG_CHOI != None) & (FLAG_ARG not in ARG_CHOICE_LIST):
            IS_ERROR = True

        return IS_ERROR
    
    # ===========================================================================
    # Housekeeping functions
    # ---------------------------------------------------------------------------
    def _force_list(self, item):
        
        item_formatted = None
        
        if (not isinstance(item, list)):
            item_formatted = [item]
        else:
            item_formatted = item

        return item_formatted
