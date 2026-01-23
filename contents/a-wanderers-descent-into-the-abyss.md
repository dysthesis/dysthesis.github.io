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
a _variable_ $x$, an _abstraction_ $\lambda x.\; t$, and an _application_ $t s$.

# The Abyss Must First Be Measured



# A Man Cannot Step into the Same River Twice...

...or can they?
