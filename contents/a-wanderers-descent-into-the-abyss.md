---
title: "A Wanderer's Descent into the Abyss"
subtitle: "Or, the Methods and Madness of the Cartography of Chaos"
ctime: 2026-01-22
mtime: 2026-01-22
tags:
  - crdt
  - database
  - systems-design
  - draft
---

# The Road to Hell is Paved with Good Intentions 

> "I am a cage, in search of a bird."
>
> -- Franz Kafka

It is only fitting that my journey had led me to this point.

The mind is designed to generate ideas rather than to store them. In my case, 
this seems doubly true: information has long escaped my grasp with disconcerting 
ease. I have therefore spent considerable time searching for a chalice of 
remembrance, to capture what would otherwise be lost. Yet the perfectionist in 
me remains dissatisfied with the results to date.

My childhood was spent, as should that of any child's, satisfied. Before me sits
a sheet of paper, and in my grasp lies a black pen. The venerable pen and paper
remains peerless in the realm of flexibility -- nothing compares to it in its
capacity to bend to the shape of the mind. Yet it was not merit that shackled my 
hand to the pen and my gaze to the paper, but ignorant bliss. My concerns were 
scant; the life of a mere child presented no heft to seek might.

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

> "Who are you then?"
>
> "I am part of that power which eternally wills evil and eternally works good."
>
> -- Johann Wolfgang von Goethe, _Faust_, First Part

Of course, it would only be honest to preface the following sections with the
following disclaimer: that this endeavour is almost entirely the fruit of my own
internal pedant. I've tried almost every note-taking-adjacent software that are
available in the market, and is nothing but trivial nitpicks that I can raise 
with a lot of them. If I were to be eternally bound to [Obsidian], I would not 
be dissatisfied.

[Obsidian]: https://obsidian.md

# A Man Cannot Step into the Same River Twice...

...or can they?
