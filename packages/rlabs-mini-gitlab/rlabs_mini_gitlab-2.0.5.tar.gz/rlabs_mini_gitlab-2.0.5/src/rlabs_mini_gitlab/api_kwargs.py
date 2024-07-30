#
# Copyright (C) 2024 RomanLabs, Rafael Roman Otero
# This file is part of RLabs Mini Gitlab.
#
# RLabs Mini Gitlab is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RLabs Mini Gitlab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with RLabs Mini Gitlab. If not, see <http://www.gnu.org/licenses/>.
#
'''
    API Kwargs

    Query parameters are passed in Kwarg format to the API methods
'''

import inspect
from typing import Any, Dict
from typing import Type

def remove_current_function_params(cls, kwargs: Dict[str, Any]) -> None:
    '''
        Remove Current Function Params

        Removes any parameters from kwargs that are part of the method signature
        for the calling method.

        Example:

           if the method signature is:

              def my_method(param1, param2, param3):
                pass

            and kwargs is:
                {
                    "param1": "value1",
                    "param2": "value2",
                    "param3": "value3",
                    "param4": "value4"
                }

            then kwargs will be:
                {
                    "param4": "value4"
                }

        Args:
            method (function): The method to inspect.
            kwargs (dict): The kwargs to remove parameters from.
    '''
    # Get the current frame and the calling method
    frame = inspect.currentframe()
    try:
        # Get the method one level up the call stack (this function's caller)
        method_name = frame.f_back.f_code.co_name
        # Get the method reference from the class
        method_ref = getattr(cls, method_name)
        # Remove parameters from kwargs
        param_names = inspect.signature(method_ref).parameters
        for param in param_names:
            kwargs.pop(param, None)
    finally:
        # Always delete the current frame to avoid reference cycles
        del frame

def remove_grandparent_function_params(
    cls: Type,
    kwargs: Dict[str, Any],
) -> None:
    '''
        Remove Grandparent Function Params

        Removes any parameters from kwargs that are part of the method signature
        for the grandparent method.

        Example:

           if the grandparent method signature is:

              def grandparent_method(param1, param2, param3):
                pass

            and kwargs is:
                {
                    "param1": "value1",
                    "param2": "value2",
                    "param3": "value3",
                    "param4": "value4"
                }

            then kwargs will be:
                {
                    "param4": "value4"
                }

        Args:
            cls (type): The class containing the grandparent method.
            kwargs (dict): The kwargs to remove parameters from.
    '''
    # Get the current frame and the grandparent frame
    current_frame = inspect.currentframe()
    grandparent_frame = current_frame.f_back.f_back

    # Get the grandparent function name
    grandparent_function_name = grandparent_frame.f_code.co_name

    # Get the grandparent method from the class
    grandparent_method = getattr(cls, grandparent_function_name)

    # Get the signature of the grandparent method
    grandparent_signature = inspect.signature(grandparent_method)

    # Get the parameters of the grandparent method
    grandparent_params = grandparent_signature.parameters

    # Remove parameters from kwargs that are in the grandparent method's signature
    for param in grandparent_params:
        if param in kwargs:
            del kwargs[param]
