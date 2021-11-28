

def formatName(firstName, lastName) :
  firstName = firstName.title()
  lastName = lastName.title()

  # print(firstName)
  # print(lastName)

  return f"{firstName} {lastName}"

print(formatName("akshunn", "sharma"))