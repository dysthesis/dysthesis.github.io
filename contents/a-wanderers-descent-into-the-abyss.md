---
title: "A Wanderer's Descent into the Abyss"
subtitle: "Or, the Methods and Madness of the Cartography of Chaos"
ctime: 2026-01-22
mtime: 2026-01-23
tags:
  - crdt
  - database
  - systems-design
  - draft
---

# The Road to Hell is Paved with Good Intentions 

![_Christ's Descent into Hell_, by Follower of Hieronymus Bosch](../assets/img/christs-descent-into-hell.jpg)

> "I am a cage, in search of a bird."
>
> <footer>Franz Kafka</footer>

It is only fitting that my journey had led me to this point.

The mind is designed to generate ideas rather than to store them. In my case, 
this seems doubly true: information has long escaped my grasp with disconcerting 
ease. I have therefore spent considerable time searching for a chalice of 
remembrance, to capture what would otherwise be lost. But the perfectionist in 
me remains dissatisfied with the results to date.

My childhood was spent -- as should that of any child's -- satisfied. Before me 
sits a sheet of paper, and in my grasp lies a black pen. The venerable pen and 
paper remains peerless in the realm of flexibility -- nothing compares to it in 
its capacity to bend to the shape of the mind. Yet it was not merit that 
shackled my hand to the pen and my gaze to the paper, but ignorant bliss. My 
concerns were scant; the life of a mere child presented no heft to seek might.

Alas, the fate of man is to be banished from Eden. A child does not remain a
child forever.

Befitting of a hellish penitentiary seized directly from the depths of Kafka's
personal Tartarus (a place one would otherwise refer to as "high school"), I was
soon thrust into a fresh world of hurt. No longer is the faithful pen and paper
enough, and the stakes soon became too high for abandon. Thus began my first
steps out of the garden, out in search for the chalice.

Unsurprisingly, my first foray landed me in the realm of [Notion]. An honourable
first try, it was leaps and bounds ahead of mere pen and paper in its 
organisational capabilities, with the ability to assign arbitrary, structured
attributes to pages and summon them with a mere query into tables. In retrospect,
it is also rather convenient compared to my later tools of choice: it is always
available[^1], and sharing and collaborating does not involve an arcane ritual
sacrificing the blood of virgins[^2]. Though, that comes with the territory of 
being a restrictive, proprietary tool locked into a server. Just like that, one 
would see the first cracks forming in the foundations of this marvellous glass 
castle.

If it has not been made painfully obvious, the Achilles' heel of Notion had been
offline access capabilities[^3]. It's also painfully inflexible: it has been
designed with a specific workflow in mind, and it is nigh impossible to bend it
to fit any other. Not that I can integrate external tools with it without jumping
through [a few hoops](https://developers.notion.com/) (why can't I run [ripgrep]
through my _own_ data again?). Worst of all, [it] [is] [painfully] [slow].[^4]

What Notion did show me, however, is that there is a way: perhaps not back to
the Garden, but onwards, to the Promised Land. Where numbers and letters may 
order itself neatly in a single-file line. Where text may sing to a tune 
conducted by queries. Where the Adamic language may once again be spoken.

Taking a bite into the forbidden fruit, one begins to fall. Down, and down, into
the abyss.

[Notion]: https://notion.so
[ripgrep]: https://github.com/burntsushi/ripgrep
[it]: https://www.reddit.com/r/Notion/comments/12322on/i_find_notion_too_slow_for_any_serious_work_why/
[is]: https://community.thomasjfrank.com/c/help-troubleshooting/notion-is-running-slowly
[painfully]: https://community.notionapps.com/t/running-really-slow-and-buggy/568
[slow]: https://reddit.com/r/Notion/comments/1qd4ooe/does_anyone_else_find_notion_painfully_slow_or_is/
[^1]: Granted, only if you have a decent network connection.
[^2]: See the previous footnote.
[^3]: This would later be [introduced on the August of 2025](https://www.notion.com/releases/2025-08-19), long after I have
then discovered far greener pastures.
[^4]: This is not just my own lack of patience speaking (though it is partly
responsible as well): [slow application response times can interrupt one's flow
of thought and focus](https://www.nngroup.com/articles/response-times-3-important-limits/).

# One Must Imagine Sisyphus Happy

![_Sisyphus_ by Titian, 1549](../assets/img/Punishment_sisyph.jpg)

> "Who are you then?"
>
> "I am part of that power which eternally wills evil and eternally works good."
>
> <footer>Johann Wolfgang von Goethe, <em>Faust</em>, First Part</footer>

Of course, it would only be honest to preface the following sections with the
following disclaimer: that this endeavour is almost entirely the fruit of my own
internal pedant. I've tried almost every note-taking-adjacent software that are
available in the market, and is nothing but trivial nitpicks that I can raise 
with a lot of them. If I were to be eternally bound to [Obsidian] or [Emacs
Org-mode], I would not 
be dissatisfied.

![How Standards Proliferate -- xkcd #927](../assets/img/standards.png)

Why then, one might ask, would I go through such lengths to make yet another
system? Simply, because I can. By both endeavour and fortune, I have been 
granted the knowledge and ability to write my own software; would it not be a
waste not to put it to use? After all, the best works are not the children of
profit, but passion.

There is no further reason beyond that. After all, we get into the habit of 
living before acquiring the habit of thinking.[^5]

[Obsidian]: https://obsidian.md
[Emacs Org-mode]: https://orgmode.org/
[^5]: Albert Camus, _The Myth of Sisyphus_.

# A Problem Well-Stated Is a Problem Half-Solved

![_Melencolia I_ by Albrecht Dürer, 1514](../assets/img/melencolia_i_albrecht_durer.jpg)

> "It is foolish to answer a question you do not understand."
>
> <footer>George Pólya, <em>How to Solve It.</em></footer>

In his book, _How to Solve It_, Pólya argued that there are four steps to solve
a problem. One must first understand the parameters to the given problem, namely

- what are the unknown,
- what are the data,
- what conditions must we maintain, and
- is it possible to satisfy these conditions.

Only then can we seek for a plan, which we do by seeking for _ideas_. Every idea
transmutes the state or formulation of the problem, and thus we wish to find 
some conjuration of ideas which transmutes our initial problem to the desired,
solved state.[^6]

A well-formulated plan is for naught if left unattempted -- an obvious next step.
Here, Pólya emphasised the verification of each step: one may see that the step
is correct, but can they also _prove_ so? Proving can be done in one of two ways,
either

- _intuitively_, by examining each atom of the step in question  until any doubt 
  of its correctness has been cleared, or
- _formally_, by deriving a chain of argument from a set of formal rules and 
  axioms.

With regards to this, a personal remark would be on what we should do in the
event of realising that our step is incorrect. A falsifying proof is just
a formulation of another, auxiliary problem: given the original problem, our 
progress on solving it, and our incorrect step, along with the falsifying proof, 
what change should be made to the incorrect step, or even the _plan as a whole_, 
to render it correct? Once this auxiliary problem is solved, we may resume with 
the execution of the now-revised plan.

Finally, one must review the problem alongside the newfound solution upon the
successful completion of it, in order to reap the fruits of their efforts when
the next problem arrives. Similar to how we verify each step during the 
execution of the plan, we must now verify the result as a whole. One method with
which Pólya suggested we do so is by attempting to derive the results in with a
different manner:

> "And as we prefer perception through two different senses, so we prefer 
> conviction by two different proofs: _Can you derive the results differently?_
> We prefer, of course, a short and intuitive argument to a long and heavy one:
> _Can you see it at a glance?_"
>
> <footer>George Pólya, <em>How to Solve It.</em></footer>

After verification, what is left to do is to ask oneself if the results or 
methods from this problem for some other problem. This will become the _ideas_
which we derive our plans for our next problem for. In other words, whereas
planning involves the _application_, or _specialisation_, of our ideas, our
review involves the _abstraction_ of our results and methods into generalisable
ideas. [^7]

Hence, we hereby seek to solve the problem: _What makes a good note-taking 
system, and how does one implement it?_ The remainder of this article will 
involve the first two steps of problem-solving: we will examine the stated 
problem, and devise a plan to solve it. Later articles (once the code have been
written) will cover the latter two, namely the execution and review steps.

[^6]: One may notice parallels between this and machine-assisted theorem proving
using languages such as [Isabelle](https://isabelle.in.tum.de/) or
[Lean](https://lean-lang.org/), where a theorem is proven by assembling
[_tactics_](https://leanprover.github.io/theorem_proving_in_lean/tactics.html),
which are rules for rewriting the formulation of the problem from one state to
another.
[^7]: Likewise, this is analogous to the formulation of computation in 
$\lambda$-calculus as a term defined by the inductive definition, consisting of 
a _variable_ $x$, an _abstraction_ $\lambda x.\; t$, and an _application_ $t\; s$.

# The Abyss Must First Be Measured

> "Beware that, when fighting monsters, you yourself do not become a monster.
> For when you gaze long into the abyss, the abyss gazes also into you."
>
> <footer>Friedrich Nietzsche, <em>Beyond Good and Evil.</em></footer>

We begin with an examination of the problem itself. _What are the unknown?_ Why,
it is a specification of what constitutes a _good_ note-taking system, of course.
Then, _what are our data?_ Well... _nothing_. Everything must start from
somewhere, I suppose. Let us do so, then, with the construction of an auxiliary 
element[^8], then, in the form of the most fundamental definition of a 
note-taking system.

I am of the opinion that there are two, otherwise equally correct approaches to 
the specification of a system: whether top-down, _i.e._ from a purely logical
view, going down the layers of abstraction to a desired level, or bottom-up,
which is its inverse.

Personally, I am more partial to the former, as the logical view is an arguably
concrete, upper ceiling to the layeyrs of abstraction. The inverse may not be
necessarily true; while by most definitions, assembly and binary would the the
botoom floor of abtraction for control and data respectively, there are
vanishingly few cases in which one would necessarily trouble themselves with
such low-level implementation details. Thus, while one would always have to
consider the logical implementation of a system, it is on a case-by-case basis
which one wouldd decide what their floor of abstraction is.

We will therefore begin with the logical definition of a note-taking system. The 
goal here is to distil the definition down to [purely mechanism, without any
policy].[^9] In other words, our definiton should be able to model any policy or
system, _e.g._ Zettelkasten, Cornell, _etc._ Sparing all but the most fundamental 
requirements, a note-taking system is a store of information, from which a user 
can enter and retrieve information. 

Here, Pólya suggests introducing suitable notation; one should find it adequate 
to denote a note-taking system $S$ as a quadruple

$$
S = (\Sigma, \Alpha, \oplus, \rho),
$$

where

- $\Sigma$ is the state space of the store of information,
- $\Alpha$ is the space of the atoms of information, and
- $\oplus$ and $\rho$ are functions which append and reduce, or query information 
  from $\Sigma$ respectively; that is,

$$
\begin{align}
  \oplus&: \Sigma \times \Alpha \to \Sigma\\
  \rho&: \Sigma \times \Alpha \to \Sigma.
\end{align}
$$

A key difference in the invariants maintained between the input function 
$\oplus$ and the reduction function $\rho$ is that

- for $\oplus$, the output $\sigma'$ must be a strict superset of the input 
  $\sigma$, and
- for $\rho$, the output $\sigma'$ must be a strict subset of the input 
  $\sigma$.

<!-- This may have some formalisation in term algebra:  -->
<!-- https://en.wikipedia.org/wiki/Term_algebra -->

We may observe that there exists a necessary relation between $\Sigma$ and
$\Alpha$: since $\Sigma$ is a store of one or more $\Alpha$, then it 
must be some structure of $\Alpha$. That is, $\Sigma$ must be defined with
respect to $\Alpha$. It may be possible to formalise this as a term algebra,
such that $\Sigma$ is some term algebra $\mathcal{T}(\Alpha)$ over $\Alpha$.

As this is our only construct so far, this will be one of our axioms. We must,
therefore, rely on intuition to convince ourselves of its correctness. We may
do so by drawing comparisons with existing systems and softwares. Let us begin
with the most basic system, the pen and paper. In a pen-and-paper system, there
exists two operations, namely

- _writing_ to the paper with the pen, and
- _reading_ the inscriptions on the paper with one's eyes.

Therefore, we may map the paper to $\Sigma$ as a structure of inscriptions of
ink, rendering the latter as our $\Alpha$. Writing, as the addition of ink
to the paper, can be mapped to a function taking the paper and inscription as
inputs, and returning a paper with it inscribed -- a superset of the original
sheet. It is therefore our $\oplus$.

However, it may be less obvious how _reading_ maps to $\rho$. But it may become
more apparent if we introduce a new sheet of paper as an auxiliary construct. On
it is inscribed some instruction, say, "find the opening paragraph of Beowulf".
One may therefore read said instruction, find the opening paragraph of Beowulf,
and inscribe it verbatim on a new sheet of paper. Hence, one would have taken in
a piece of paper (the text of Beowulf) and an inscription (the instructions to
find its opening paragraph), and outputted another sheet of paper with the
instructed content -- that it is a subset of the original text should be 
apparent.

Mapping this onto a digital system should also be straightforward: instead of
inscriptions, it is bytes, and instead of sheets of papers, it is CPU caches,
RAM, or hard drives. But then, how does this hold up to the logical abstractions
built upon it?

<!-- We may want to go through with proving that this problem has an optimal
substructure: if \Sigma, \Alpha, \oplus, and \rho are optimal, then S is
optimal. -->

One noticeable difference between content on paper and on the computer is the 
ability to erase. If one makes a mistake, it is a mere keystroke away to delete
it. How does this map to our system?

Interestingly, there are two viable mappings for erasure. Both are equally
satisfactory with respect to the definition, but have significantly different
implications. We may first notice the straightforward mapping to our $\rho$
function, which, given some atom $\alpha \in \Alpha$, returns a strict subset
$\sigma'$ of the original store $\sigma$. Deletion may therefore be defined as
some function $\text{del}: \mathbb{S} \times \Alpha \to \mathbb{S}$, such that

$$
\text{del} = \lambda \alpha S. (\rho\; (f\; \alpha)\; \sigma, \Alpha, \oplus, \rho) \text{ where }\sigma\in S,
$$

where $f$ is some function mapping the atom $\alpha$ to the correct expression
for its deletion. Therefore, given some $S = (\sigma, \Alpha, \oplus, \rho)$ and
$S' = (\sigma', \Alpha, \oplus, \rho)$ such that $S' = \text{del} \alpha S$, we
have that $\alpha\in\sigma$ but $\alpha\not\in\sigma$.

An astute reader may make two observations from the above, namely that

- the deletion operation is expressible as an atom $\alpha \in \Alpha$, and
- that $\text{del}$ above is irreversible and permanent.

These observations may hint at the construction of an alternative mapping for
deletion: _why not simply add the atom for the deletion operation into the store?_
This is plausible given the right structural representation of $\Sigma$, which
we will get to later.[^10]

As such, we may also map deletion as

$$
\text{del} = \lambda \alpha \;S. (\oplus\; (f\; \alpha)\; \sigma, \Alpha, \oplus, \rho) \text{ where }\sigma\in S.
$$

The consequence of the above construct is that deletion is a reversible 
operation: one may insert another atom that deletes said deletion atom, or 
reduce the store with $\rho$ to permanently remove said atom.

To give shape to what would otherwise be a highly abstract notion, we may
analogise 

- the first construction of $\text{del}$ to the rewriting of sheet of notes on 
  another sheet, _without_ the desired inscription, and
- the second construction of $\text{del}$ to the crossing-out of some erroneous
  section of text.[^11]

Hence, we may have arrived at a satisfactory intuition on the correctness of our
construct $S$, but there is another, profound consequence of it: the 
expressibility of actions as atoms $\alpha\in\Alpha$ grants us the ability to
store not just the space, but time. The second construction of $\text{del}$ is
able to reverse any action at any given time. This is not to say that the first
construction does not have its uses, however. As much as one would like to
pretend that storage is infinite (and it might as well be, given the size of
modern hard drives), we may eventually hit a storage limit and need to remove
information _permanently_.

[purely mechanism, without any policy]: https://en.wikipedia.org/wiki/Separation_of_mechanism_and_policy
[^8]: George Pólya, _How to Solve It_, Part III. Short Dictionary of Heuristic.
[^9]: As an aside, the separation of mechanism and policy is a [core principle
in the architecture of microkernels](https://www.cs.vu.nl/~ast/books/mos2/).
[^10]: **Hint:** it's [CRDTs](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type).
[^11]: I'm aware that this is not a perfect mapping: one cannot cross out the
cross to undo it. Such is the restriction when it comes to a physical medium.

# A Man Cannot Step into the Same River Twice...

...or can they?

