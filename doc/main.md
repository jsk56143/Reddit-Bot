# Main Documentation

## Description

**Author**: Josh Kim

**Date Created**: 12/17/2021

**Date Modified**: N/A

**Purpose**: 

* This is the main script that will be run on the cloud platform. It checks that new posts (submissions) don't break the rules and does other helpful stuff.

## Current features
1. (Teaser) - Replies to teaser posts reminding users that some teaser content is allowed, but if the final product is not of the genre, it's better suited for the Music Recommendations Thread.
2. (Discussion) - Checks if in-depth discussion posts are greater than 450 characters.
3. (Variety) - Checks if [RAW] or [ENG] or [ENG SUB] is at the end of the title. This is probably the only way to check for title violations for Variety content.
4. (Music Video, Audio, Live, Album) - Checks if posts are link posts
5. (Music Video, Audio, Live, Album) - Checks if " - " is in the title. This is probably the only way to check for title violations for music posts.

## Future features
1. Add teaser image posts to collection. If full and current month hasn't changed, make a new one. If month has changed, make a new month colleciton.
 * Problem: Determining song's genre
2. Add underground songs to collection. Might involve Spotify, YouTube, and SoundCloud API. 