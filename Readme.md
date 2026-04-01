# Probability Puzzles 2

A collection of programming solutions and simulations for probability puzzles drawn from Donald Knuth's *The Art of Computer Programming* (TAOCP). Each puzzle wraps a classic algorithmic concept in a narrative story, and each script verifies the analytical solution through Monte Carlo simulation.

## **Course I: The Theorems**

### **Permutations & Sorting**

**[The Careless Typesetter's Toll](scripts/careless_typesetter.py) (Problem 1A)**

A careless typesetter drops a pristine, perfectly ordered manuscript consisting of N numbered pages. He gathers them up blindly, resulting in a completely random permutation. Realizing his mistake, he decides to sort the manuscript using a very tedious method: he reads through the stack, and whenever he sees two adjacent pages that are out of order, he swaps them. He continues doing this until the entire manuscript is sorted.

*What is the expected number of swaps the typesetter will have to make to restore the manuscript of N pages? For bonus points, what is the probability that he will have to make exactly zero swaps, or exactly one swap?*

**AOCP Connection:** This puzzle asks for the expected number of **inversions** in a random permutation of length N. It fundamentally models the average-case runtime of Bubble Sort or Insertion Sort.

---

### **Stream Selection**

**[The Cautious Alchemist's Vial](scripts/cautious_alchemist.py) (Problem 2A)**

An alchemist discovers a magical, ephemeral spring in the forest. The spring sporadically ejects glowing vials of a rare elixir. The alchemist knows the spring will eventually dry up, but he has no idea how many vials it will produce in total. The alchemist only has one lead-lined box, meaning he can only carry exactly one vial home. As each vial emerges, he must immediately decide whether to place it in his box (discarding the one currently in the box, which shatters instantly) or let it dissolve into the earth.

*What probabilistic strategy must the alchemist employ as each vial emerges so that, when the spring finally dries up, every vial produced had an equal, uniformly random chance of being the one in his box?*

**AOCP Connection:** This is a narrative wrapping of **Algorithm R (Reservoir Sampling)**, originally attributed to Alan Waterman. It explores how to maintain a uniformly random sample from a data stream of unknown length using a simple, dynamic fractional probability.

---

### **Binary Search Trees & Quicksort**

**[The Fractious Tour Guide](scripts/fractious_tour_guide.py) (Problem 3A)**

A tour guide is tasked with organizing a chaotic group of N tourists of uniquely different heights. He employs a peculiar method: he selects one tourist entirely at random and asks them to stand in the center. He then commands everyone shorter than the center tourist to form a group to the left, and everyone taller to form a group to the right. He then points to the left group, randomly picks a center person for them, and splits them again. He does the same for the right group. He continues this recursive fracturing until everyone is standing alone.

*Consider the tourist who is the k-th shortest in the group. What is the expected number of times this specific tourist will be commanded to move to a new "left" or "right" group before they are finally chosen to be a center pivot themselves?*

**AOCP Connection:** This puzzle investigates the average number of comparisons required to find the k-th smallest element in a randomly constructed **Binary Search Tree**, which is mathematically identical to the depth of an element during a randomized **Quicksort**.

---

### **Hash Tables & Linear Probing**

**[The Infinite Hashway](scripts/infinite_hashway.py) (Problem 4A)**

Miss Hashway is a librarian in a vast, circular library containing M empty pedestals arranged in a giant ring. She is tasked with placing N magical books. For each book, she rolls an enchanted M-sided die to determine which pedestal to place it on. If that pedestal is empty, she places the book. If it is already occupied by a previous book, she simply walks clockwise to the very next pedestal. If that is occupied, she checks the next, and so on, until she finds an empty spot to place the book.

*If the library has M = 1000 pedestals, what is the expected number of occupied pedestals she will have to inspect (skip over) when attempting to place exactly the 500th book?*

**AOCP Connection:** This is an exploration of **Linear Probing** in hash tables. The math behind the clustering effect in linear probing is one of the most beautiful and surprising results in computer science, showing that the expected probe length grows dramatically as the load factor increases.

---

### **Cycle Structure of Permutations**

**[King Permutio's Dungeon](scripts/king_permutio.py) (Problem 5A)**

The mad King Permutio has imprisoned 100 knights in 100 separate, locked cells. He takes the 100 unique keys to the cells, shuffles them thoroughly in a sack, and places exactly one random key on the table inside each cell. Each knight is allowed to look at the key in their room. They realize that the keys form a chain: the key in Cell 1 might open Cell 47, the key in Cell 47 might open Cell 12, and so on.

*What is the exact probability that the keys are distributed such that they form one single, massive chain? That is, starting from Cell 1 and following the keys, you would visit every single one of the other 99 cells before finding the key that leads back to Cell 1?*

**AOCP Connection:** This puzzle explores the **Cycle Structure of Random Permutations**. The mathematics of cycles within permutations is foundational to cryptography, sorting, and analyzing the structural properties of arrays. (The answer is surprisingly elegant: exactly 1/N, or 1/100).

---

## **Course II: The Boundaries**

### **Permutations & Sorting**

**[The Archivist's Epiphany](scripts/archivists_epiphany.py) (Problem 1B)**

An eccentric royal archivist is presented with a hopelessly shuffled stack of N historical decrees, each bearing a unique, absolute chronological date. He begins reading them one by one from the top of the stack. Because he is easily impressed, he only bothers to transcribe a decree into the Royal Log if it is strictly *older* than every single decree he has read so far in the stack.

*As N grows agonizingly large, what is the expected number of decrees the archivist will actually transcribe? Furthermore, what is the precise probability that in a stack of 100 decrees, he transcribes *exactly* two of them?*

**AOCP Connection:** While the first puzzle looked at out-of-order pairs (inversions), this puzzle looks at **left-to-right maxima** (or minima) in a random permutation. It elegantly models the average number of times a "current maximum" variable must be updated when scanning an unsorted array. The expected number is the N-th Harmonic number (H_N ≈ ln N), and the exact probabilities are beautifully governed by the Stirling numbers of the first kind.

---

### **Stream Selection**

**[The King's Council](scripts/kings_council.py) (Problem 2B)**

A traveling King decides to form a Council of Wisdom consisting of exactly K=5 advisors. As he travels the endless roads of his kingdom, he constantly meets new wise men and women. The King will travel forever, and he wants to ensure that at any given moment, every wise person he has *ever* met has an equal, uniform probability of currently holding a seat on the Council.

*When the King meets the N-th wise person (where N > 5), what is the exact probability he must use to decide whether to invite them to the Council? If they are invited, how should he choose which of the current 5 advisors to dismiss? Finally, over an infinitely long journey, what is the expected number of times a sitting advisor is fired?*

**AOCP Connection:** This elevates the previous puzzle to the full, generalized **Algorithm R (Reservoir Sampling)**. It proves that to maintain a uniform sample of K items from a stream of N, the N-th item should be selected with probability K/N, and it should replace a randomly chosen member of the current reservoir. The expected number of replacements scales logarithmically.

---

### **Binary Search Trees & Quicksort**

**[The Indecisive General](scripts/indecisive_general.py) (Problem 3B)**

A general commands a chaotic army of N battalions, all of strictly different battle strengths. To organize them, he chooses one battalion uniformly at random to stand in the center. All battalions weaker than the center are ordered to the left valley; all stronger to the right valley. He then delegates: he commands the left valley to repeat this exact same random splitting process, and the right valley to do the same. This continues until battalions cannot be split further. A battalion that ultimately ends up with *no* subordinates (no one weaker than them in their local group, and no one stronger) is designated a "Frontline Unit".

*What is the expected number of Frontline Units (battalions with zero subordinates) generated by this chaotic chain of command?*

**AOCP Connection:** The previous puzzle explored the *depth* of a node in a random Binary Search Tree. This puzzle asks for the expected number of **leaf nodes** in a randomly generated BST. The math yields a stunningly simple, exact, and counter-intuitive result: for N inserted elements, you expect exactly (N+1)/3 leaves.

---

### **Hash Tables & Linear Probing**

**[The Sleepy Knights of the Round Table](scripts/sleepy_knights.py) (Problem 4B)**

The legendary Round Table has M chairs. M knights return from a quest, exhausted, entering the hall one by one. Each knight has a favorite chair (chosen uniformly at random). When a knight enters, he goes to his favorite chair. If it is empty, he collapses into it and sleeps. If it is already occupied by a previously arrived knight, he is too tired to argue; he simply walks clockwise to the very next chair. If that is occupied, he checks the next, and so on, until he finds an empty chair to sleep in.

*Since there are exactly as many knights as chairs (M knights, M chairs), the table will eventually be full. What is the precise probability that the *very last* knight to enter the hall gets to sleep in his actual favorite chair?*

**AOCP Connection:** This is a framing of the famous **Parking Problem** (originally posed by MacMahon, but heavily utilized by Knuth to analyze hash table clustering). Because linear probing causes occupied slots to merge into massive, gravitationally attractive clusters, the last few insertions face brutal pile-ups.

---

### **Cycle Structure of Permutations**

**[The Spies Who Watched Me](scripts/spies_who_watched_me.py) (Problem 5B)**

A paranoid secret society consists of N spies. The Director assigns each spy to heavily surveil exactly one other spy in the society. To be "fair," the Director places the names of all N spies in a hat, and each spy draws one name to watch (if they draw their own name, they just watch their own back). Because everyone is watching exactly one person, the surveillance network naturally forms closed, independent loops.

*On average, how many independent surveillance loops will form in the entire society? Furthermore, what is the probability that Agent 007 finds himself in a perfectly mutual standoff—watching the exact same person who is watching him (a loop of exactly size 2)?*

**AOCP Connection:** Where the previous puzzle asked for the probability of the extreme edge case (one giant cycle of size N), this puzzle asks for the fundamental average behavior: the **expected number of cycles** in a random permutation. Just like the left-to-right maxima puzzle, the answer is intimately tied to the Harmonic numbers, revealing a deep structural symmetry between scanning an array and the closed loops of permutations.

---

## **Course III: The Symmetries**

### **Permutations & Sorting**

**[The Dispatcher's Dilemma](scripts/dispatchers_dilemma.py) (Problem 1C)**

A royal courier must deliver N sealed edicts to N distinct manors located along a single, endlessly long, one-way road heading East. The manors are numbered 1 to N based on their distance from the castle. The sleepy dispatcher hands the courier the N edicts in a completely random, shuffled pile. The courier reads the top edict, rides East to that manor, and delivers it. He then reads the next edict. If the next manor is further East, he continues down the road. But if the next manor is *behind* him (further West), he cannot turn around; he must return all the way to the castle, rest for the night, and begin a brand new journey East the next morning.

*On average, how many distinct journeys (days of riding) will the courier need to make to deliver all N edicts?*

**AOCP Connection:** While previous puzzles looked at individual out-of-order pairs (inversions) or new maximums, this puzzle asks for the expected number of **ascending runs** in a random permutation. It is the mathematical foundation of "Natural Merge Sort," which exploits pre-existing sorted sub-segments in data. (The elegant answer: he expects to make exactly (N+1)/2 journeys).

---

### **Stream Selection**

**[The Fickle Philanthropist](scripts/fickle_philanthropist.py) (Problem 2C)**

A wealthy, eccentric patron of the arts visits an endless, magical gallery of N paintings. He has only one frame in his carriage, meaning he can only take one painting home. He employs the cautious alchemist's strategy (Algorithm R) from our very first course to ensure that every painting he sees has an equal 1/N chance of being his final choice. However, the patron's porters are growing incredibly tired. Every time he decides to temporarily "keep" a new painting, they must physically swap it with the one currently in the carriage frame.

*Assuming N is incredibly large, how many times, on average, will the exhausted porters be forced to swap the painting in the carriage frame?*

**AOCP Connection:** We know the *strategy* of Reservoir Sampling, but this asks for its *cost*. The expected number of times the reservoir variable is overwritten is exactly the N-th Harmonic number minus one (H_N - 1). It wonderfully connects the physical act of stream sampling back to the "Left-to-Right Maxima" math of our previous course.

---

### **Binary Search Trees & Quicksort**

**[The Bureaucrat's Burden](scripts/bureaucrats_burden.py) (Problem 3C)**

A sprawling empire of N civil servants must be organized into a strict chain of command. The Emperor picks one servant uniformly at random to be the Supreme Minister. All servants with less seniority form the Left Faction; all with more form the Right Faction. Each Faction randomly selects a Sub-Minister to lead them, splitting their subordinates again, recursively, until everyone has a boss. The "Burden" of a civil servant is defined as the exact number of bosses they must go through to reach the Supreme Minister.

*If you sum together the Burden of every single civil servant in the entire empire, what is the expected total Burden?*

**AOCP Connection:** We previously looked at the depth of a specific node, and the number of leaf nodes. This puzzle asks for the **Total Internal Path Length** of a random Binary Search Tree. This is arguably the single most important metric in Volume 3, as it perfectly equates to the total number of comparisons required to sort an array of N items using average-case Quicksort: roughly 2N ln N.

---

### **Hash Tables & Linear Probing**

**[The Phantom's Promenade](scripts/phantoms_promenade.py) (Problem 4C)**

Return to the circular library of M pedestals. Miss Hashway has already placed N magical books using her method: rolling an M-sided die, and walking clockwise until she finds an empty pedestal to place the book. The library is now highly clustered. A wandering phantom enters the library looking for a specific, ancient tome. He rolls his own M-sided die to determine where to start looking. He checks the pedestal. If a book is there, he checks the title, and if it's not his tome, he floats clockwise to the next pedestal. He will keep checking books until he reaches an *empty* pedestal, at which point he will conclude the book isn't in the library and vanish.

*Assuming the book is indeed *not* in the library, how many pedestals, on average, will the phantom have to inspect before he hits an empty one and gives up?*

**AOCP Connection:** We explored the probability of the *last* insertion, but this asks for the expected cost of an **Unsuccessful Search** in a Linear Probing hash table. Knuth's derivation of this formula—showing that the expected probes for an unsuccessful search is roughly (1/2)(1 + 1/(1-α)²) where α = N/M—is considered one of the great triumphs of algorithmic analysis, perfectly quantifying the catastrophic penalty of table clustering.

---

### **Cycle Structure of Permutations**

**[Sir Lancelot's Loop](scripts/sir_lancelots_loop.py) (Problem 5C)**

We descend one last time into King Permutio's dungeon. 100 prisoners, 100 cells, 100 randomly shuffled keys. We know from the first course that the keys form closed loops. We are now observing one specific prisoner: Sir Lancelot, locked in Cell 1. He dreams of his escape route. He hopes that his cell's key will lead to a very short loop—perhaps the key in his room opens Cell 4, and the key in Cell 4 opens his own Cell 1 (a loop of exactly 2).

*What is the exact probability that Sir Lancelot finds himself in a loop of exactly length K, where K is any specific integer between 1 and 100?*

**AOCP Connection:** We previously calculated the chance of a single massive cycle of length 100 (which was 1/100), and the expected total number of cycles (H_100). But this puzzle asks for the distribution of the cycle containing a *specific* element. The math resolves to a result of staggering, poetic simplicity: the probability that Sir Lancelot is in a cycle of length 1 is 1/100. The probability of length 2 is 1/100. The probability of length 47 is 1/100. For a specific element, *every possible cycle length is equally likely*.
