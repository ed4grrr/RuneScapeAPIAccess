import abc
from typing import Any


class IParser(metaclass=abc.ABCMeta):
    """
    This interface requires a method to parse an API-output string into a Python usable Data
    structure for easy consumption by the end user.

    This class demonstrates a close approximation of interfaces found within other languages. This code
    was adapted from the code found here (https://realpython.com/python-interface/).

    To make other interfaces, copy the code within this class. Any new methods added must
    raise the NotImplementedError AND be registered in the dunder method subclasshook
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        This method is used to register functions that this interface requires to make
        Python's "duck typing" work appropriately when testing if an object has correctly
        implemented the required methods.

        This is an approximation of how interfaces are implemented within other languages. This class takes advantage of
        "Duck Typing" to emulate interfaces in Python. The code seen below is used to register what methods the implementing
        classes must override to be seen as a parser within this module.


        To add a new function to the interface's contract, the user must create a new class that implements (or in
        Python, just inherits) and the new class must override the Parse_API_Response method. The new function must be
        registered to this method as seen below with the example "Parse_API_Response".

        To add another concrete function named "Your_Function", add the following code
        just after the last added function (in this case, Parse_API_Response) to the boolean expression seen below:

        and hasattr(subclass, "Your_Function") and
        calllable(subclass."Your_Function")

        To remove a function, just delete the registration within this method and delete the function
        declaration and return statement.

        All of this must be done, of course, in source code.
        """
        return (
            hasattr(subclass, "Parse_API_Response")
            and callable(
                subclass.Parse_API_Response
            )  # to add a another method, you must add another
            or
            # hasattr/callable combo with the new method name
            NotImplemented
        )

    @abc.abstractmethod
    def Parse_API_Response(self, response: str)-> Any:
        """
        Parses an API response in a particular format
        @param response: the text response from the API
        @return a python-friendly object containing the data obtained from the API. The exact type will depend on how the
        relevant IParser implementing class and its return type.
        """
        raise NotImplementedError
