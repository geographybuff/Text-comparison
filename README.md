# Text-comparison

Check out Text compare.ipynb for the Jupyter Notebook where the program is hosted.
Determines whether two texts were written by the same author using a Keras neural network with 15 inputs:
1: 12 (6x2) individual attributes (frequencies of periods, commas, unique words, apostrophes, words 7 letters or more, words 10 letters or more)
2: 3 shared attributes (percentage of shared words, shared two word phrases, and shared three word phrases

Corpus is composed of four passages each from eight English-language prose authors from four continents, written over a period of 303 years.
Passages range over a wide variety of subjects, including romantic novels, political science, dystopia, fantasy, and humor.
Passages range from roughly 1500-7000 words in each file. Occasionally multiple chapters are included in one file so as to pass 1500 words.

George Orwell: 1984 Chapter 1, 1984 Chapter 2, Animal Farm Chapter 1, Animal Farm Chapter 2

J. R. R. Tolkien: The Hobbit Chapter 1, The Hobbit Chapter 2, The Fellowship of the Ring Foreword, The Fellowship of the Ring Prologue

Charles Dickens: Great Expectations Chapter 1, Great Expectations Chapter 2, The Detective Police Part 1, The Detective Police Part 2

Jane Austen: Pride and Prejudice Chapters 1-2, Pride and Prejudice Chapter 3, Persuasion Chapter 1, Persuasion Chapter 2

Mahatma Gandhi: Hind Swaraj Chapter 1, Hind Swaraj Chapters 2-3, A Guide To Health Chapters 1-3, A Guide to Health Chapters 4-5

Mark Twain: Tom Sawyer Chapter 1, Tom Sawyer Chapter 2, An American Vandal Abroad, Among the Spirits

John Locke: A Letter Concerning Toleration Part 1, A Letter Concerning Toleration Part 2, Some Thoughts Concerning Education Part 1, Some Thoughts Concerning Education Part 2

Thomas Hobbes: Leviathan of Man Chapters 1-2, Leviathan of Man Chapter 3, The Elements of Law Chapters 1-2, The Elements of Law Chapter 3

Also includes a heatmap correlogram showing an adjusted comparison score for the three comparison attributes,
and six bar graphs for the six individual attributes.
