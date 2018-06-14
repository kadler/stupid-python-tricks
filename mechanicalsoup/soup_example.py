import mechanicalsoup

# based off https://github.com/MechanicalSoup/MechanicalSoup/blob/master/examples/expl_httpbin.py
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://httpbin.org/")

# click on the link containing "forms"
browser.follow_link("forms")

browser.select_form('form[action="/post"]')
browser["custname"] = "Kevin"
browser["custtel"] = "507-555-1985"
browser["custemail"] = "me@example.com"
browser["size"] = "medium"
browser["topping"] = ("bacon", "cheese")
browser["comments"] = "Deliver to my hammoc in the back yard"

response = browser.submit_selected()
print(response.json())

