string = "skdjfkjaskdfjklksjdflksjflkjsojfoweijowifjeofwejoiwjflsjflsjdlfjslfjlsddjfoldfpowejefjfjwejfowejfjwejfwejewepriwepirupiowuperiodnclksncmnfoiweuropijndkjlashlluehopancpjwjehfpuhwpcn9perhw0jf"
k = 3
t = []
for i in range(0, len(string), k):
    t.append(string[i : i + k])
print(t)
