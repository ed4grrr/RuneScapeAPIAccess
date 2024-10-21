import abc
class iParser(metaclass=abc.ABCMeta):
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

        To add a new function, it must be decorated with @abc.abstractmethod. This new function
        Must then be registered to this method as seen below.

        To add another abstract function named "Your_Function", add the following code
        just after the last added function to the boolean expression seen below:

        and hasattr(subclass, "Your_Function") and
        calllable(subclass."Your_Function")

        "Your_Function" should also be decorated with "abc.abstractmethod", AND the only code should
        be "return NotImplementedError"

        To remove a function, just delete the registration within this method and delete the function
        declaration and return statement.
        """
        return (hasattr(subclass, 'Parse_API_Response') and
                callable(subclass.Parse_API_Response)  or # to add a another method, you must add another
                                                          # hasattr/callable combo with the new method name
                NotImplemented)

    @abc.abstractmethod
    def Parse_API_Response(self, response: str):
        """
        Parses an API response in a particular format
        @param response: the text resopnse from the API

        """
        raise NotImplementedError