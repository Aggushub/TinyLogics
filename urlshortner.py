Sure! Here's your code with **line-by-line explanation** and **comments** added:

```python
# Import the 'pyshorteners' library which provides URL shortening services
import pyshorteners 

# Prompt the user to enter a URL and store it in the variable 'url'
url = input("Enter URL :-")  

# Create a Shortener object, use the TinyURL service to shorten the URL,
# and print the shortened version to the screen
print("URL after shortening :-", pyshorteners.Shortener().tinyurl.short(url))
```

---

### 🔍 Detailed Explanation:

#### `import pyshorteners`

* This line imports the `pyshorteners` module.
* `pyshorteners` is a Python library that interfaces with various URL shortening services like TinyURL, Bitly, etc.

#### `url = input("Enter URL :-")`

* This line asks the user to input a URL.
* The user’s input is saved as a string in the variable `url`.

#### `pyshorteners.Shortener().tinyurl.short(url)`

* `pyshorteners.Shortener()` creates a shortener object.
* `.tinyurl` selects the TinyURL shortening service (built into the module).
* `.short(url)` sends the original URL to TinyURL's API and returns the shortened version.

#### `print("URL after shortening :-", ...)`

* Prints the message and the resulting shortened URL on the screen.

---

### 🧪 Example:

**Input:**

```
Enter URL :- https://www.example.com/very/long/url/path
```

**Output:**

```
URL after shortening :- http://tinyurl.com/abcd1234
```

Let me know if you want a version that handles errors (like invalid URLs or no internet)!
