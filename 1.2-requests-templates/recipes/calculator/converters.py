class RecipeConverter:
   regex = r'^(omlet|pasta|buter)'
   def to_python(self, value: str) -> str:
       return value

   def to_url(self, value: str) -> str:
       return value