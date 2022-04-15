"""
Just a reminder of who to email the info to because I keep forgetting. 
"""

# This will be who I need to email to let them know that I've sumbitted VBS
email_list = ("To: ashley.n.ollison@ricoh-usa.com",
              "CC: jessica.davis@ricoh-usa.com")


def print_emails():
    """Just a quick print call to show who to email."""
    print("\nEmail the following people to let them know this was submitted:\n")
    for each in email_list:
        print(each)
