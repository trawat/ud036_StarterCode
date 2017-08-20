# Movie Trailer Website

Allows its users to watch their favourite movies and its trailors.

## Getting Started

1. Clone [project](https://github.com/trawat/ud036_StarterCode.git) from GitHub to your local machine.
2. Open the project in your favourite IDE.
3. Or, if you prefer command line then open Python shell on your local machine and navigate to the directory `ud036_StarterCode`.
4. Now, run or execute `entertainment_center.py` file which is the starting point.

### Prerequisites

* [Download](https://www.python.org/downloads/) and install latest Python version available on your local.
* Mac OS users can follow [this](http://docs.python-guide.org/en/latest/starting/install/osx/) link. And, for setup steps on Window OS - please follow [this](https://docs.python.org/3/using/windows.html) guide.

### Running

* Navigate to the cloned project base directory from command prompt or open `entertainment_center.py` file if you are using an IDE.
* Execute `entertainment_center.py` file -

  _Command Line_
```
ud036_StarterCode $ python entertainment_center.py
```

* Running the `entertainment_center.py` will create `fresh_tomatoes` HTML file in the projects base directory and open it in a web browser.

*  `fresh_tomatoes` displays a list of my favourite movies. Clicking on the movie banner open a dialog to play the movie trailor.

### Modification

It is possible to modify the default list of movies to suit anyones taste. Follow, the steps listed below for the same.

* Open `entertainment_center.py` in your favourite editor.
* Edit `movie_data` list.

_For example_

First, create an entry as below -

```
['my_movie_name', 'my_movie_banner_image_location','my_movie_trailor_video_location']
```
above, all three inputs should be inside single quotes. Movie banner image and its trailor video can be publicly accessible URL or absolute path on your local machine.

Then, add this entry to `movie_data` or replace any existing entry.

_Sample entry_
```
["Dumb And Dumber", "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg", "https://www.youtube.com/watch?v=l13yPhimE3o"]
```

_Before modification_

```
movie_data = [
              ['movie1_name', 'movie1_banner_image', 'movie1_trailor_path'],
              ['movie2_name', 'movie2_banner_image', 'movie2_trailor_path'],
              ['movie3_name', 'movie3_banner_image', 'movie3_trailor_path']
             ]
```

_After modification (Replacing an existing entry)_

```
movie_data = [
              ["Dumb And Dumber", "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg", "https://www.youtube.com/watch?v=l13yPhimE3o"],
              ['movie2_name', 'movie2_banner_image', 'movie2_trailor_path'],
              ['movie3_name', 'movie3_banner_image', 'movie3_trailor_path']
             ]
```

### License

This project is released under [MIT License](https://choosealicense.com/licenses/mit/).

### Acknowledgments
* Udacity instructor notes.
