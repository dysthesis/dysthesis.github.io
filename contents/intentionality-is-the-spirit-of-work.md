---
title: "Intentionality is the Spirit of the Work"
ctime: 2026-01-28
mtime: 2026-01-28
tags:
  - practices
  - notetaking
---

**Note.** Unfinished draft, mainly just a braindump.

As I have been thinking a lot about how to build [my notetaking system], a key
subject of ponderance have been on the limits of the use of automation, and in
particular, language models. In particular, what should it be allowed to do, and
what should it not. 

This is especially important since, as I've [previously written], _automation
offsets the need for discipline._ Another important idea is that of discipline,
or the lack thereof, being the harbinger of rot -- the notes repository of one
who lacks discipline is more likely to be unorganised, and more importantly,
_unorganisable_, as they would likely have not even curated sufficient context
and metadata for any form of automation to organise it for them with reasonably
acceptable quality (it is given by the premise that such a person would also not
be inclined to organise it themselves).

[my notetaking system]: ./a-wanderers-descent-into-the-abyss.md
[previously written]: ./commits-as-experiments.md

# Drawing a Line

Instinctually, I've been driven to be more comfortable with the use of, say,
embedding models to calculate the semantic similarity of the content, but not
with any form of agentic mechanisms to explore, or god forbid, _write_ the
contents of my notes. The question, then, is _why_? What is the precise line
which separates the two?

This question serves a twin purpose: that is,

- it is the _falsification criteria_ of my aformentioned hypothesis; if a precise
  discriminant cannot be found, then it is but a mere gut feeling, and
- it will be a necessary guideline for the implementation of my system (when I
  finish building its building blocks and finally get around to doing so™️).

# The Machine Does Not Intend

![Internal IBM Training from 1979](../assets/img/a-computer-can-never-be-held-accountable.jpg)

I've recently came across an [interesting piece of computing history from Simon
Willison's Weblog]: a page from an internal IBM training which says

> A COMPUTER CAN NEVER BE HELD ACCOUNTABLE
>
> THEREFORE A COMPUTER MUST NEVER MAKE MANAGEMENT DECISION

This begs the question, then: why can't one hold the computer accountable? After
all, despite its [many](https://www.youtube.com/watch?v=kSno1-xOjwI), [_many_](https://blog.trailofbits.com/2026/01/13/lack-of-isolation-in-agentic-browsers-resurfaces-old-vulnerabilities/) faults, computers
are now capable of performing actions derived from some, albeit _limited_, form
of intelligence.

I think the answer lies in the computer's _lack of intention_. For some -- arguably
_most_ -- definitions of what constitutes intention, computers cannot exhibit it.
Insofar as any technological advancements have brought us, intention remains the
sole domain of humans.

This captures with it the heart of the discrimination at the thesis of this
post: **the use of agentic language models to explore or write your notes is a
misguided attempt to automate intention.** This is something that cannot -- and,
I'd argue, _should not_ -- be automated away.

This is, admittedly, an unsatisfactory answer. It leaves the definition vague,
abstract, and largely in the realm of highfalutin philosophy, rather than a
formal, rigorous construction.

[interesting piece of computing history from Simon Willison's Weblog]:
https://simonwillison.net/2025/Feb/3/a-computer-can-never-be-held-accountable/

# Don't Automate Away Your Intentions

When one, say, runs Claude Code on their Obsidian vault and asks it to collect
information on some topic, they are leaving the computer to fill in the dots.
Natural language is imprecise[^1]; consequently, any instructions provided to the
agent will contain some gaps with respect to one's true intentions. It is then
left to the agent to make assumptions to bridge these gaps by itself.

A second loss of intent would be on the decisionmaking regarding the exploration
path taken while gathering the prerequisite information. It is up to the agent
to decide where to go, and what, among its findings, to include and what to 
exclude. Not only does this lead to a loss of control on the human's end on the
final output, but it deprives from one the opportunity for a serendipitous 
encounter with non-obvious, _interesting_ connections between ideas (for some
definition of interesting).[^2]

I don't suppose that it would be necessary to provide an exposition on why this
also applies to allowing the language model to write in your notes, as the
mapping should be self-explanatory and literal.

[^1]: See Dijkstra's writing, ['On the foolishness of "natural language programming"'](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html).
[^2]: It is, after all, one of the key strengths of atomic, relational note-taking
systems, such as the Zettelkasten.
