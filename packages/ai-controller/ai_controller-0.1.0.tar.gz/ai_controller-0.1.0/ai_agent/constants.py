PROMPT_FOR_FINDING_FUNCTION = """You need to understand the context and meaning of the input-text and functions descriptons provided and return me the most closest function which matches with the input text.
Note: You should only respond in this format {{"function_name": "", arguments: []}}, 
Please do not add any additional text or formatting. If not matching functions found then provide '_' in function_name with empty arguments
Input-text: '{input_txt}'
Functions name-description obj(key=function_name and value=function_description): {obj}"""