# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Styling Flask

Author: Kevin Coyle

-----

### Learning Objectives
*After this lesson, you will be able to:*
1. Explain what HTML and CSS are
2. Write basic HTML
3. Write basic CSS

---------
HTML and CSS Intro

---
<!-- Slide 1
Talking Points
-->
## HTML & CSS

HTML tells browsers what content to display, and CSS tells browsers how that content should look.

---
## Intro to HTML
<!-- Slide 2

-->
HTML means Hyper Text Markup language.

Using HTML allows developers to change achieve font, color, graphic, and hyperlink effects on web pages.


---
## Without HTML
<!-- Slide 3
Talking Points
-->
Without HTML

[Harry Potter Profile: Bland](https://codepen.io/thisisdrewlove/pen/MXLgqW)
---
## With HTML
<!-- Slide 4
Talking Points
-->

With HTML

[Harry Potter Profile: Fancy!](https://codepen.io/thisisdrewlove/pen/rKPNPY?editors=1000)

---
## How do I make an HTML document?
<!-- SLIDE 5
- Now that you know a little about styling HTML documents, let's look at how to create one.
- Every HTML document starts with `<!DOCTYPE html>`. If students ask why, you can explain that historically, HTML doctypes declared the set of rules to be considered good HTML (error checking, etc.). Now we just need it so that everything works.
- Then you have the <html> and </html> elements. These are known as the root elements
- <head> element comes next. This is all of the stuff that you don't want your audience to see, like keywords and page descriptions for websites.
- then <meta charset="utf-8"> which declares your character set to UTF-8. This means that you'll be able to render just about every character in almost every major language.
- the <title> element is what names your page. It's used in the name for the browser tab and when you bookmark a page
- the <body> element is all the content you want your audience to see. -->

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
</head>
<body>
<p> Here's my awesome content! </p>
</body>
</html>
---
## Anatomy of an element
<!-- Slide 6
> The basic building blocks of an HTML document are elements
> Elements consist of an opening tag, content, and closing tag
> The tag tells the web browser how to render, or display, the content
-->

* Opening tag: `<p>`
* Content: text, image, video, other elements
* Closing tag: `</p>`

---
## Basic tags
<!-- Slide 7
Talking Points
There are many kinds of tags that help create structure and flow for your webpage
Let's review some of the most basic tags
Review how different header sizes use different numbers
<h1> is the largest, and <h6> is the smallest
<h1> and <h2> are the most common
-->
Common Tags:
* bold: `<b>bold</b>`
* paragraph: `<p>paragraph</p>`
* header: `<h1></h1>`

---
##Harry Potter Example
<!-- Slide 8
Talking Points
Point out where tag is used.
Review the structure of a tag, opening tag, content, closing tag
-->

[Harry Potter Profile](https://codepen.io/thisisdrewlove/pen/rKPNPY?editors=1000)

---

##Now you try
<!-- Slide 9
Encourage students to experiment with the tags.
Their profile doesn't have to be in the same format as the Harry Potter
profile.
-->
Using the tags below, create a profile for yourself.

Include: name, about me, experience, and hobbies

Common Tags:
* bold: `<b>bold</b>`
* paragraph: `<p>paragraph</p>`
* header: `<h1></h1>`

---
##HTML Attributes
<!-- Slide 10
> Building on our knowledge of tags, let's start to explore the next topic: HTML Attributes
> Some tags require attributes in order to work properly
> One tag that requires the attribute, is the <img/> tag
> the src is the name, and the "image.com" is the value
-->
An HTML attribute provides extra information to the browser about the tag

There are two parts
* name
* value

`<img src="image.com"/>`

---
##img tag example
<!-- slide 11
Talking Points
-->

[Harry Potter Profile with Pic](https://codepen.io/thisisdrewlove/pen/OEdJwL?editors=1000)
---

##Add an img tag
<!-- slide 12
Talking Points
-->

Add an img tag to your profile.

Use the format below.

Change the value, "image.com", to a url of your choice.

`<img src="image.com"/>`
---

##Intro to CSS
<!--
slide 13

--



Styling Flask

### What Does this look like?

<!-- SLIDE
- Our hello world Flask app is beautiful. But not everyone else knows how to look at it and fully appreciate its beauty  
- In this lesson we are going to focus on HTML -->

Our hello_world.py app looks like

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

---

### What is HTML?
<!-- SLIDE 1
HTML - Hyper Text Markup Language is not a programming language.  
  Let's try to modify our hello world app by bolding the "hello" part.
  -HTML
	- We use an opening "tag" with the B, and the closing tag, which is the same thing, and a forward slash.
              <b>Hello</b>
	- From tag to tag is known as an element, and the "hello" part is known as the content.
	- Flask can actually have HTML right in the app.
	- While it wouldn't be efficient to always write our HTML like this, we can get an idea of some styling elements called Tags
	-->

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<b>Hello</b>, World!'
```
---

### Adding this into our app
<!-- SLIDE 4
- It's your turn!
- We will get into how to render our HTML doc in a later lesson. However, first we want you to try your hand at writing HTML.
- You can see how your content renders directly in the browser for now... just double click on index.html after you've saved your changes
- We need to put the index.html in a folder because flask looks for our html files in a folder called "templates." More on that in a later lesson on templates. -->

Take our simple HTML and save it to a file called "index.html" in a folder called "templates."

Next, we'll modify content.

---  


### CSS

<!-- SLIDE XX
	- CSS is used to style how documents are produced to users. HTML is the most common language.
	- Let's modify our HTML document by adding in the <link> element.
	- Then we'll create a simple css file that modifies our HTML doc
	- h1 refers to the <h1> header in the HTML document
	- p refers to the p element in our HTML document. 	
	- In each CSS, notice that we have a key/value pair system
	- In css, each of these key/value pairs are called declarations.
	- We put the style.css in a folder called static because flask looks for our css files in that folder.
	- Lastly, we include a bracket to let our flask app search for our css file in that static folder. More on brackets and templates in a later lesson.
-->

We'll modify our index.html:
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My cool foodie site!</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css')}}">
  </head>
  <body>
    <h1>Hello Whirrled!</h1>
    <p>If music be the food of love, play on</p>
  </body>
</html>
```
Also create a simple CSS and save it to a file called "style.css" in a folder called "static."
```
h1 {
  color: yellow;
  background-color: green;
  border: 1px solid black;
}

p {
  color: red;
}
```

---

### Your turn!

Modify your css file. Here's some ideas:
- Try changing the colors in your css file
- Do some quick independent research. See if there are other key/value pairs (other than "color" and "background-color") that you can change.

---
## Review
We covered Styling Flask:
1. What HTML and CSS are
2. Writing basic HTML
3. Writing basic CSS

---
