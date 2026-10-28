from pyscript import document

# this are the artists from drill 2
grade7 = {"Drake", "The Weeknd", "Bruno Mars", "Ariana Grande"}
grade8 = {"Kendrick Lamar", "Billie Eilish", "Lana Del Rey", "SZA"}
grade9 = {"The Beatles", "The Neighbourhood", "Arctic Monkeys", "Radiohead"}
grade10 = {"Tyler The Creator", "Frank Ocean", "Taylor Swift", "Sabrina Carpenter"}

# we use the union operator to combine all the artists
master_set = grade7 | grade8 | grade9 | grade10

def verify_candidate(event):
    """Main event function: triggers when button is clicked to verify membership status."""
    
    # from here we get the inpur the user gives and then find it
    first = document.getElementById("first_name").value.strip().title()
    last = document.getElementById("last_name").value.strip().title()
    full_name = f"{first} {last}".strip()

    # we use the full name to see if they are in the master set and then if it's true or not
    is_member = full_name in master_set

    # since we dint use any if/then loops, we use bollean
    messages = {
        True: f"Congratulations {full_name}! You are now part of the Singing club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    # this is how we get the output
    document.getElementById("results").innerText = messages[is_member]
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""