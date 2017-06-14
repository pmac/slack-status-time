# Slack Status Time

Automatically update your slack status with the current time in your timezone.

This isn't probably all that useful, but I enjoyed making it. It will update your Slack status
to your local hour, and set the status emoji to that hour's clock face.

## Usage

Best way to go is to use Docker. It's all set to go. You just need to generate a Slack token
at their [API legacy token page](https://api.slack.com/custom-integrations/legacy-tokens), and
then pass that in as an the argument to the `run-update` script.

```bash
$ ./run-update xoxp-XXXXXXXX-XXXXXXXX...
```

The default timezone for the script is "America/New_York", but you can set any other by setting the `TZ`
environment variable:

```bash
$ TZ="America/Los_Angeles" ./run-update xoxp-XXXXXXXX-XXXXXXXX...
```

The script will build the docker image and run the script.

## Cron

Best way to run this is via cron. Here's what I did:

Create a script that has your token in it (and never give it to anyone).

```bash
$ mkdir -p ~/bin
$ echo "#!/bin/bash -e

export TZ=America/New_York
/path/to/slack-status-time/run-update <your-slack-token-here>
" > ~/bin/slack-status-update
$ chmod +x ~/bin/slack-status-update
$ crontab -e
```

That last command will open an editor. Put this in it:

```cron
0 * * * * ~/bin/slack-status-update
```

It should now run every hour on the hour.

Enjoy!
