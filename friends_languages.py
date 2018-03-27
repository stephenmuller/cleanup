favorite_languages = {"jen":"c#", "john":"python", "chris":"sql"}

friends = ["jen", "john"]
for name in favorite_languages.keys():
	print(name.title())
	
if name in friends:
	print(" hi " + name.title() + ", i see your favorite language is" + favorite_languages[name].title() + "!" )
	 
