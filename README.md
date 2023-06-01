# My Project - Code Snippet Manager: Instructions

## Momentum Boot Camp Project 10

Skills:

- using models.py to create multiples classes: User, Snippet, Language, and Tag
- ability for new users to register
- funcionality for logged in users: view profile with only their snippets, duplicate other user's snippets, ability to log in and out, display of user's information in the header
- ability to copy code from a snippet to the user's clipboard
- search bar for snippets
- tracks the number of time a snippet has been duplicated, and duplicated snippets link to parent snippet
- Snippets can only have one author, but be connected to multiple users

## Below are Project Directions

Steps to open app:

1. Download the repo
2. Run `pipenv install`, `pipenv shell`, `python manage.py migrate`, and `python manage.py runserver`
3. Open the server url in your browser

While logged out you can view Snippets, Languages, and Tags. There is also a search bar in the upper right corner of the browser to find relevant snippets.
If you haven't created an account yet you will need to register before you can log in. When logged in you have more interaction available:

1. Snippets: You can view a list of all snippets, create/edit/delete snippets, duplicate a snippet someone else has authored, and view a user profile with the snippets you have authored. You can also copy a snippet's code to you clipboard when viewing a snippet's details page.
2. Languages: You can view a list of all languages, and create/edit/delete languages.
3. Tags: You can view a list of all tags, and create/edit/delete tags.

Other notes:

1. The app name in the header will link to the snippet list.2) While logged in the username will display in the header.
2. You can view the number of times a snippet has been duplicated in snippet details.
3. If a snippet is a duplicate of another snippet, then the snippet details will have a link out to the parent.
4. Multiple users can be connected to a snippet, but it only has one author.

# Choose a Project

This week, you will be on a small team working on a project.

Use your combined creativity and good judgment to make decisions as you work. Users expect to see some common features in web applications. If they are not mentioned in the project's description, you should still do them. For example: in the code snippet application, users should have avatar images. You don't have to handle file uploads yourself -- you could use Gravatar with [django-gravatar](https://github.com/twaddington/django-gravatar) -- but you need some way of handling that.

In addition to those small features, come up with your own features to make your project unique. You will likely use this project in your portfolio, so make it something you can be proud of.

No starter repo is provided, so you will have to run the `django-admin` commands to create a new project.

# Rules for all projects

- Your application should be styled. It should be usable and aesthetically neutral, at a minimum. You can use a library or you can write custom css, or both. It is up to you.
- Your application must include a README.md file with instructions on how to run it. [Take a look at this site on README basics](https://www.makeareadme.com/) for a good markdown template you can follow, and links to example READMEs.
- Your application should be able to run from scratch by downloading the repo, running `pipenv install`, `pipenv shell`, `python manage.py migrate`, and `python manage.py runserver`. If there are any other steps necessary, please put them in the README.md file.

## Stretch goal for each project: trying new things

Teams should consider trying something they don't know how to do on their project. This could be a Python or JavaScript library they haven't used before or a feature of Django they haven't tried.

# The Projects

Your team should choose one of these options.

## Option 1: Code Snippet Manager

You need a good way to manage snippets of code you reuse often. You are going to build a web application that has these goals:

- Logged in users can add code snippets.
- Logged in users can search their own code snippets and get results.
- Each user has a profile page that shows their public code snippets. Other users can copy a snippet with one click, adding it to their library of snippets.

### How snippets work

A snippet has code (required), a language (required), a title (optional), and whatever other fields make sense. Some ideas to consider: a description or a list of tags.

If you copy a snippet by clicking the copy button (or whatever UI element is used for this purpose), there's a link back to the original snippet. The easiest way to do this is with a foreign key. One should be able to see how many times a snippet has been copied.

The reason why we copy snippets instead of "favorite" them is that they can change. The original snippet creator can edit their snippet; the copying user can edit their copy.

### How search works

Search should look for terms in the title, in other fields like a description or tags, and in the language field. If I search for "javascript auth," I should see any snippets I have about authentication using JavaScript. See [search](https://docs.djangoproject.com/en/3.2/topics/db/search/) in the Django documentation for some ideas.

### How much of this is JavaScript?

This can vary, but the two parts that _definitely_ need JavaScript are syntax highlighting and copying a code snippet to your clipboard.

For syntax highlighting, check out [Prism.js](https://prismjs.com/) or [Highlight.js](https://highlightjs.org/).

See [this article on native browser copy to clipboard](https://css-tricks.com/native-browser-copy-clipboard/) for ideas on how to copy to clipboard.

## Option 2: Flashcards

You want to make an application to help people learn via flashcards. You are going to build a web application that has these goals:

- Logged in users can create multiple decks of flashcards, each with a prompt or question and an answer.
- Logged in users can quiz themselves on a deck.
- Success and failure for each card is recorded.

### How decks and cards work

A user can have multiple decks of flashcards. Each deck has a title. Each flash card has a prompt or question and an answer.

When a user is quizzing themselves on a deck, they _do not_ have to type in answers. They are shown the prompt, they click to see the answer; they then mark whether they answered it correctly or not. They should see one card at a time.

When the user marks success or failure on a card, this should be recorded.

The cards should be shown in a random order at a minimum. A preferable method would be to use something like [the Leitner system](https://www.virtualsalt.com/learn10.html) for flash cards. This system uses review times; you could use that, or just use the idea of multiple boxes, with cards in lower boxes coming up more often.

### Creating decks and running through decks

This application has two very distinct parts: creating decks and cards and then running through those decks. This is a natural place to split work. Do not forget to make creating decks and cards an easy-to-use experience.

### How much of this is JavaScript?

"Flipping" a card (you don't have to animate a card flip, although if you do, that's very cool) will almost certainly require JavaScript.

You could have a page load in between cards and reduce your amount of JavaScript. Depending on how you do this, it could also record success or failure, eliminating most of your JavaScript.
