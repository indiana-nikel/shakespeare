# shakespeare

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Overview

William Shakespeare is one of the most famous playwrights in history, writing 35+ plays and 150+ sonnets over his lifetime. Looking specifically at his plays, Shakespeare had three distinct categories: tragedy, comedy, and history. His characters have unique stories and telling messages that students still analyze to this day. Some of these plays even become best-selling movies (Disney's The Lion King is essentially Shakespeare's Hamlet)! So what if there were more of these plays?

My approach to generating new works of Shakespeare was to use a recurrent neural network (RNN) built of long short-term memory (LSTM) units. Since plays, and text in general, are meant to be read in a particular order, LSTMs are able to learn the patterns of what would come next after a specific word. I used RNNs with LSTMs over a more simple model, such as hidden Markov models (HMM), because they are able to pick up on more intricate patterns of text. One example is that HMMs may open a parentheses but could never close it, or close it sometime far in the future. RNNs with LSTMs are much less prone to this problem.

In this model, I pass in all of Shakespeare's plays, pulled from [http://shakespeare.mit.edu/](http://shakespeare.mit.edu/).

## Dependencies (pip install)

```
keras
tensorflow
numpy
```

## Usage

To train the model, I wrote [onefile.py](src/onefile.py) to combine the individual plays into one file. You can edit this file to combine solely historical plays or comedy plays.

To train the model:

```
python3 src/textgen.py train "data/shakespeare.md"
```
The result will output a series of weight files under the `model/` directory. Feel free to use the ones provided since training on a GPU took close to 48 hours.

To generate text:

```
python3 src/textgen.py gen --weightsfile "model/weights-shakespeare.md-100-20-1.2386.hdf5" "data/shakespeare.md"
```
The result will output a markdown file in the `output/` directory with 2000 characters (can be changed, see [textgen.py](src/textgen.py)).  

## Results

I have included 10 output files, all unique generations of Shakespeare. Here is my favorite passage that I have read so far:

```
SCENE III. The same. A room in the fire.

    Enter MARIA and FABIAN

OLIVER

    I cannot see thee.

    Exit
```

It's not perfect, but the results are promising (and a bit hilarious at times)!
