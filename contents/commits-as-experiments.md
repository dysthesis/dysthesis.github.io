---
title: "Commits as Experiments"
subtitle: "On Earning Our Place in the Pantheon of the Sciences"
ctime: 2026-01-27
mtime: 2026-01-27
tags:
  - ideas
  - practices
  - draft
---

**Disclaimer.** This is only an idea that I've had, not something I've built 
yet. I am interested in building this in the future, however, likely on top of
[the abyss](./a-wanderers-descent-into-the-abyss.md).

# On Superstition and Guesswork

![_The witch no. 1_ by Joseph E.](../assets/img/2560px-Salem_witch2.jpg)

It is standard practice for one to compose a Git commit message to communicate
intent. The idea is that, _what_ changes are being made can be trivially
deduced by reading the diff -- explaining that in the commit message would be
a mere regurgitation of the obvious. The commit message should, therefore,
explain what could not otherwise be explained by the mechanistic artifacts,
namely _intent_. We may see what changes you have made, yes, but _why_ have you
done so? In other words: _What goal is it that you seek to achieve with this?_

Of course, this is not enforced by any sort of mechanism, it's simply good
practice. This much is plain for anyone to see. What is not as obvious, however,
is the lack of _rigour_ in this practice, and consequently, the lack of
_provenance._

A mere `git commit -m "(perf) a bunch of optimisations"` does not communicate
what the impact is on the resulting code as a whole. This is not only about what
exact components are being targeted by the change, what metric it is seeking to
change, and what the actual impact is, but also _what the impact is on the rest
of the codebase._ Sure, this may have improved, say, the performance of one
component, but does it come at the detriment of anything else? That is, it does
not provide the complete and reliable picture of the trade-off being made with
the given change.

This brings us to the next point, which is that even in the best of times, 
intent is often expressed in a inexact, _hand-wavy_ manner. What exactly does it
mean for the throughput of the lexing to be improved? Under what load was this
tested under, and in what conditions? Likewise, what does it mean for some
feature to be implemented? What is the acceptance criteria for completion?

More importantly, _how can we trust you?_

# To Know That You Know Nothing

![_A Philosopher Lecturing on the Orrery_ by Joseph Wright of Derby](../assets/img/Wright_of_Derby_The_Orrery.jpg)

> "The aim of science is not to open the door to infinite wisdom, but to set a
> limit to infinite error."
>
> <footer>Bertolt Brecht, <em>Life of Galileo</em>.</footer>

In addition to brewing what I would imagine to have been some delightful cups
of coffee[^1], the coffeehouses of 17th- and 18th-century England brewed in them
some of the first sparks of the Age of Enlightenment. It was the cornucopia 
which brought us many advancements which we largely take for granted today[^2]
-- individual liberty, separation of church and state, and natural rights, to
name a few.

At the centre of this revolution was the notion of _epistemic humility:_ the
virtue of enumerating candidly what one knows, what one does not know, and what
one _can never_ know. This is the bedrock upon which the marvellous spires of
science are built on. It is the philosophical foundations of the the scientific
method, positing that theories are _valuable_ insofar as they are _falsifiable_.
Experiments are, therefore, rigorous attempts to falsify one's hypothesis, in a
paradoxical endeavour to solidify their credibility. Further progress led to the
creation of the peer review process, Enshrined with it, then, is the necessity 
of the reproducibility of one's claimed methodology results. **This is the sole
differentiator of science from superstition.**

As one should be able to deduce, computer _science_ is, indeed, a _science_.[^3]
In fact, we are situated at a vastly more fortunate position than virtually all
the other sciences -- that fortune is _accessibility_. We may construct 
experiments without the need for a mass spectrometer, microscope, or centrifuge.
Our laboratory lies at our fingertips, and over it, we reign as divine. It is
of profound shame, then, that I have not witnessed scientific rigour exercised
in comparable ubiquity as with other sciences.

Most major, notable projects are able to maintain the discipline to practice
this rigour. However, such projects remain a rarity in the grand scheme of
things; it is only those projects created and maintained by the most seasoned, 
skilled developers which are able to achieve such a feat. Unfortunately, it is
indeed a _feat_ -- one which remains unattained by the layperson.

[^1]: ![Garraway's Coffee House in Exchange Alley, London](../assets/img/Garraways_Coffee_House.jpg) 
In observance of tradition, this was written as I drank my morning cup of coffee.

[^2]: Though, given what the vicissitudes of the world has decreed for us in
recent times, perhaps not for long.

[^3]: ![Surprised Pikachu Face](../assets/img/pikachu.jpg)

# Automation is the Poor Man's Discipline

One cannot expect the fresh graduate[^4] to compare to the wise old greybeard,
as they simply have not earned a comparable quantity and quality of experience 
and learning. Even if one were to be sufficiently studious to know, in theory,
the value of such practices, it is difficult to ingrain it into one's habit
without having experienced firsthand the dire consequences of the lack thereof.
Hence, espounging discipline is simply a subpar solution to our problem.

On the contrary, let us consider the economic spectrum in which the notion of
_discipline_ lies. Discipline exists as a tradeoff for friction: the more
friction is inherent to some endeavour, the more discipline is required to
perform it, and _vice versa._ Hence, by reducing the _friction_ necessary to
build our software with scientific rigour, the less _discipline_ is needed to
perform it. We hope that this is sufficient to promote its ubiquity.

Automation, then, is the purveyor of the redution of friction, as it performs
tasks in our stead, reducing what we would otherwise must do ourselves. If we
are able to automate the collection of data, the maintenance of hygiene in our
experimentation environment, the bookkeeping necessary for provenance and
reproducibility, and other such menial chores, it would render rigour 
significantly more trivial to achieve. Furthermore, with sensitive tasks such as
the enumeration of the experimentation environment, it removes the need for
trust in humans; for example, we may enforce the hash of every binary executed
in the experiment, or use a content-addressable storage for our artifact storage.

Note that the aim is not to enforce absolute rigour and hygiene, as otherwise,
we would simply construct an experimentation harness over virtual machines such
that the _entire_ environment is perfectly verifiable and replicable. For one,
some use cases simply do not support such setups, and what we consider to be the
gold standard practice in one field may be detrimental to the quality of the
results in another. We must not fool ourselves, yet the challenge is that we are
the easiest person to fool.[^5]

No, the goal is instead to prove the other person's claim, and audit its
provenance instead of relying on the trust in their good nature. **The tool that
I envision is, therefore, envision is, therefore, one which verifies 
cryptographically the methodology and results of one's experiment with respect
to a change in source code and intended effect.** With it, one would be able to

- define a hypothesis in terms of some change in code, as well as an intended
  effect, such as some (measurably specified) improvement in performance,
  expansion in capability, and/or resolution of a gap in soundness or 
  completeness[^6] (such as bugs or vulnerabilities), and
- declare in some computer-readable format (say, TOML or JSON[^7]) a suite of
  experimentation methodology to falsify said hypothesis,

such that the tool can automate the execution of the experiment and the
collection of the resulting data. The responsible changes in code can be 
enumerated in the form of some commit or merge request. We can therefore see,
in a standardised, reproducible, and verifiable way the each hypothesis and
result. Then, even failed hypothesis can be valuable to store -- we may learn
better from our mistakes as they are recorded, allowing them to serve as prior
knowledge and explanations for any further failures.

[^4]: This is speaking from experience -- I am said fresh graduate yet to grow
the proverbial, opulent facial hair.
[^5]: <span class="sidenote-quote"> The first principle is that you must not
    fool yourself — and you are the easiest person to fool.
    </span>

    <span class="sidenote-cite">Richard Feynman.</span>

[^6]: Soundness means that anything that is false is not provable, and 
completeness means that anything that is true is provable.
[^7]: An interesting conjecture is to declare it in a proof assistant such as
Lean, Isabellle, or LiquidHaskell. A hypothesis is then declared as an axiom in
the target formal language, alongside a falsification suite and an acceptance
criteria with respect to said suite. A hypothesis that passes the criteria is
then added to the generated library of axioms, allowing one to prove theorems
on the runtime behaviour of the program. While it is true that empirical results
are finite while formal axioms are universal, the declaration of the
falsification sutie and acceptance criteria provides the necessary level of
transparency: we have declared that these theorems are built on top of some
finite empirical observation based on the given acceptance criteria -- it is
therefore only as good as such.

# Coda

> "For me, it is far better to grasp the Universe as it really is than to 
> persist in delusion, however satisfying and reassuring."
>
> <footer>Carl Sagan, <em>The Demon-Haunted World.</em></footer>
