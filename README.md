# Config file

Default to `~/.config/rstblog-tools.conf`

Overridable with `RSTBLOG_TOOLS_CONFIG` environment variable

Content:

    BLOG_DIR=/path/to/blog
    BLOG_OUT_DIR=/path/to/blog/out


# Tools

## rstblog-build

Generates the blog and serves it on localhost.

## rstblog-new

Asks a few questions and create a new post, marked as private. Offers to start
editing the post with default editor.

## rstblog-publish

Make a post public and update the `pub_date` to now. This is useful to produce
accurate dates in feeds. So that the new post appears on top when an aggregator
fetches it.

## rstblog-edit

List available posts and start editing the post with default editor.

## rstblog-deploy

Sync build output with blog out dir, commit and push the changes.
