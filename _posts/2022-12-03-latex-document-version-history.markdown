---
layout: post
title:  "LaTeX Documentation Helpers"
categories: latex, administrative
---

For files relevant to this post, please go to this [github](https://github.com/xyise/latex_version_history) repo.

# Version History
## Background

When writing a document for work purposes, it is common practice to have 
* **front page**, showing document title and key control informations such as version, author, documentation classification, etc. 
  
* section to track the document **version history**. Although different from company to company, or even team to team, it typically contains a combination of version, date, author, summary of change, etc, in a tabular form. 

Example: 

|                                   front page                                    |                                      version history                                      |
| :-----------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: |
| ![front page example](/assets/latex-doc-version-history/front-page-example.png) | ![version history example](/assets/latex-doc-version-history/version-history-example.png) |


While both front page and version history section may serve their own purposes (probably, bureaucratic and administrative reasons though), this leads to *duplications* of the same information. For example, the writer has to change the version number in two different places whenever making any changes to the document. Of course, it is not uncommon to notice having one version number in the front page and a different number in the version history section. 

## Defining Version History Command

With LaTeX, this problem can be solved by defining a version history command and keeping track of *all* vision history. 

To demonstrate how it works, we define a command `\versionDateAuthorSummary` in [here](https://github.com/xyise/latex_version_history). Whenever a new version entry is entered using this command, LaTeX updates an *array* that keeps track of all version entries. 

For example, suppose there have been 3 revisions. Then, we enter each version *in chronological order*, like this: 

```
\versionDateAuthorSummary{v0.1}{2022-01-01}{Alice}{Initial draft.}
\versionDateAuthorSummary{v0.2}{2022-01-03}{Brian}{Fixed typos}
\versionDateAuthorSummary{v1.2}{2022-01-30}{Catherine}{To share with stakeholders.}
```

This will create an array of 3 version entries. Then, all we need to do are
* For the front page, read the last version entry from the array.
* For the version history section, loop over the array and print each entry. 

In fact, the screenshots in Background section are generated through these processes. 


# Administrative Required Fields

For administrative reasons, your company or team may require you to include certain fields (e.g. version, team name, relevant committee name, contact details, classifications, etc) on the front page or a dedicated page. To make this requirement clearer to writers, we can define a command to each required field and show an instruction if it is not filled. 

For example, this defines a new command `\documentTeamName` to specify the team name. 
```
\newcommand{\@documentTeamName}{\colorbox{red!30}{Set team name by specifying \texttt{\textbackslash documentTeamName}}}
\newcommand{\documentTeamName}[1]{\edef\@documentTeamName{#1}}
```
The first line contains an instruction how to set the field if it is not yet set. 

The table below shows how the field appears in the document before and after setting this field.

|                                  front page                                  |                         version history                          |
| :--------------------------------------------------------------------------: | :--------------------------------------------------------------: |
| ![not set](/assets/latex-doc-version-history/front-page-example-not-set.png) | ![set](/assets/latex-doc-version-history/front-page-example.png) |





