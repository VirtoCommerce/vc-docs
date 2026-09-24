# Sign-in Log

The platform now keeps a durable record of every successful and failed sign-in attempt including sessions started through **Login on behalf**. 

The following logs are recorded:

| Entry point | What is recorded | 
|-------------|------------------|
|Back office sign-in and sign-out | Success <br> Wrong password <br> Unknown user name <br> Locked-out account <br> Sign-out | 
| Token endpoint, password grant | Success <br> Wrong password <br> Unknown user name <br> Locked-out account <br> Password login disabled <br> Expired password | 
| External identity provider (SSO) | Success and failure with the provider name |
| Login on behalf | Grant <br> Revert back to the operator <br> Denied attempt <br> Attempt against a user that does not exist |


To view the sign-in log:

1. Click **Security** in the main menu.
1. In the next blade, select **Sign-in log**.
1. View the logs for the past 30 minutes, 1 hour, 24 hours, and 7 days. 
1. The widgets display a short summary of sign-ins, failed attempts, signed in users, and logs on behalf of other users. The widgets are clickable:

    ![Sign-in log](media/sign-in-log.png){: style="display: block; margin: 0 auto;" }

1. Click any widget to see a detailed log:

    ![Detailed log](media/sign-in-details.png){: style="display: block; margin: 0 auto;" }

Each record carries the date, the user name as it was typed, the outcome, the failure reason if any, the sign-in type, the operator for on-behalf rows, IP address, host, user agent, store and member. Names are stored as they were at the time, so a later rename does not rewrite history. Deleting a user account does not delete their records.


## Settings

To open the **Sign-in log** settings:

1. Click **Settings** in the main menu.
1. In the search field of the next blade, type **Sign-in log** to find the settings related to the feature.
1. In the next blade, configure the following settings:

    ![Sign in log](media/sign-in-log-settings.png){: style="display: block; margin: 0 auto;" }

1. Click **Save** in the toolbar.

Your modifications have been applied.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../active-sessions">← Managing active sessions</a>
    <a href="../settings">Settings →</a>
</div>

