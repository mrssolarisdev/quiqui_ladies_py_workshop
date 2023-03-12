from enum import Enum

class ClothingTypeEnum(Enum): # Your enum needs to inherit from this class.
    """Enum containing all of the clothing types supported by our application"""
    
    PANTS = 'PANTS' # Now, every variable in your enum carries a value. It should be like an str, int, etc.
    SKIRT = 'SKIRT'
    SHIRT = 'SHIRT'
    OVERALLS = 'OVERALLS'
    
    # All methods implemented should be classmethods, as enum instances can't be created and the methods are intended to be used by the class itself.

    # As the single doublescore hints, this method "is private" and shouldn't be accessed from outside this class. It is "overriding" 
    # the _missing_ implementation from the class "Enum". Which is responsible for deciding what to do in case it cannot find an 
    # specific entry in the enum. Thus, in our implementation you could return whatever makes sense for your application.
    @classmethod
    def _missing_(cls, clothing_type) -> None:
        """
        Method that overrides the '_missing_' implementation of the class Enum. Called whenever a value being passed
        was not found among the enum members' values.
        
        Args:
            clothing_type (str): A string to be found as a value of a member in the enum.
        Raises:
            NotImplementedError: If no member with the specified value is found
        """
        # There you could return an specific entry of the enum and implement some logic depending on the context,
        # and raise an exception for some specific cases (as it might make sense in some contexts). In our case, 
        # we will just raise an exception.
        raise NotImplementedError(f"{clothing_type} clothing type doesn't exist.")
    
    # Another option could be implementing a method like this:
    @classmethod
    def from_value(cls, value) -> 'ClothingTypeEnum':
        """
        Given a specific value, returns the member of the ClothingTypeEnum with that value
        
        Args:
            value (str): A string to be found as a value of a member in the enum.
        Raises: 
            NotImplementedError: If no member with the specified value is found
        Returns:
            ClothingTypeEnum: A specific member of the enum, if found.
        """
        for cls_member in cls:
            if cls_member.value == value:
                return cls_member
        raise NotImplementedError(f"Clothing type with {value} value doesn't exist.")

    

# We can directly access the entries in the enum like this:
pants = ClothingTypeEnum.PANTS
# -------------------------------------------------------------------------------------------------------------------------------------------
# Or we can find the enum member by looking for the member with an specific value, 
# although it is not recomended, try using the enum members directly (It may depend on the context)
print(ClothingTypeEnum("SHIRT")) # returns: ClothingType.SHIRT
# -------------------------------------------------------------------------------------------------------------------------------------------
# As we implemented a method specifically for finding an enum member by its value, we could also do:
print(ClothingTypeEnum.from_value("SKIRT")) # returns: ClothingType.SKIRT
# -------------------------------------------------------------------------------------------------------------------------------------------


# Now, some general conventions:
# 1 - Do not modify the values of the enum after they are defined. Enums are intended to be constants.
# -------------------------------------------------------------------------------------------------------------------------------------------
# 2- Do not define duplicate values. Each value in an enum should be unique.
# -------------------------------------------------------------------------------------------------------------------------------------------
# 3 - Do not compare enums using the '==' operator. Instead, use the 'is' operator or the 'Enum.eq' method. 
# Example: 
print(ClothingTypeEnum.SKIRT is ClothingTypeEnum.PANTS) # False
# or:
print(ClothingTypeEnum.SKIRT.__eq__(ClothingTypeEnum("SKIRT"))) # True
# "But each member of the enum has its own value, can't I compare them?". Yes, you can compare the values, not the enum members themselves.
# Example:
print(ClothingTypeEnum.SHIRT.value == ClothingTypeEnum.SKIRT.value) # False
# -------------------------------------------------------------------------------------------------------------------------------------------
# Do not create instances of an enum using the constructor. Enums should be used as constants, not as classes that need to be instantiated.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Do not define a 'init' method in an enum. Enums are intended to be constants, not classes that need to be instantiated.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Do not define arbitrary methods or properties on an enum (create only the necessary classmethods). Enums are intended to be simple, constant values.