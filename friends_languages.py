favorite_languages = {"jen":"c#", "john":"python", "chris":"sql"}

friends = ["jen", "john"]
for name in favorite_languages.keys():
	print(name.title())
	
for name in friends:
	print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!" )
	 
