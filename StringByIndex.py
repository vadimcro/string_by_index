class StringByIndex:
    """
    A custom node to select a string from a list of up to 10 input strings
    based on a provided index. Includes fallback logic.
    """
    
    @classmethod
    def INPUT_TYPES(s):
        """
        Defines the input types for the node.
        - 'index_value': The integer used to select which string to output.
        - 'default_string': The fallback string if all else fails.
        - 'string_0' to 'string_9': The 10 optional string inputs.
        """
        
        # This creates a dictionary for 10 optional string inputs
        # (string_0, string_1, ..., string_9)
        # They are 'optional' so they appear as widgets you can type in
        # OR as connectors you can link nodes to.
        string_inputs = {
            f"string_{i}": ("STRING", {"default": "", "multiline": True})
            for i in range(10)
        }
        
        return {
            "required": {
                "index_value": ("INT", {"default": 0, "min": -100, "max": 100}),
                "default_string": ("STRING", {
                    "default": "default fallback prompt",
                    "multiline": True
                }),
            },
            "optional": string_inputs
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "select_string"
    CATEGORY = "Logic/Switches" # You can change this to any category you like

    def select_string(self, index_value, default_string, **kwargs):
        """
        The main logic function.
        - 'index_value' and 'default_string' come from 'required' inputs.
        - '**kwargs' will contain all 'optional' inputs (string_0 to string_9).
        """
        
        # 1. Collect all string inputs into a list
        # We fetch them from kwargs using the same names we defined in INPUT_TYPES
        string_list = []
        for i in range(10):
            # .get() will safely return the value or None if it's not found
            # (though it should always be found, even as an empty string)
            string_list.append(kwargs.get(f"string_{i}", ""))

        output_string = ""
        use_fallback = False
        
        # 2. Check if the int value is within the limits (0 to 9)
        if 0 <= index_value < 10:
            selected_string = string_list[index_value]
            
            # Check if the *selected* string actually has text
            if selected_string is not None and selected_string.strip():
                # .strip() removes whitespace. If anything is left, the string is valid.
                output_string = selected_string
            else:
                # The selected string is empty or just whitespace, so we trigger fallback
                use_fallback = True
        else:
            # The index value is outside the 0-9 range, so we trigger fallback
            use_fallback = True
            
        # 3. Handle all fallback logic in one place
        if use_fallback:
            # Check if string_0 (the zero index) has any text
            string_0_val = string_list[0]
            if string_0_val is not None and string_0_val.strip():
                output_string = string_0_val
            else:
                # If string_0 is also empty, use the 'default_string' input
                output_string = default_string

        # 4. Return the result as a tuple
        return (output_string,)

# This is the standard boilerplate to register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "StringByIndex": StringByIndex
}

# This is the name that will appear in the ComfyUI node menu
NODE_DISPLAY_NAME_MAPPINGS = {
    "StringByIndex": "Select String by Index"
}