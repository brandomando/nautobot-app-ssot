# Using the App

## General Usage

### Dashboard

The plugin dashboard UI can be accessed from the **Plugins > Single Source of Truth > Dashboard** menu item in Nautobot.

![Dashboard](../images/dashboard_initial.png)

The left side of the dashboard lists all discovered Data Sources and Data Targets. In a fresh installation this will include the "Example Data Source" and "Example Data Target"; when you install additional data synchronization Jobs they will be automatically discovered and included in the dashboard as well.

The right side of the dashboard lists the ten most recent data syncs executed (if any) and summarizes their outcomes.

### Data Source/Target details

From the dashboard UI, you can click on the name of any given Data Source or Data Target to access a detailed view of the integration between this system and Nautobot.

![Data Source detail view](../images/data_source_detail.png)

This view lists the configuration (if any) of the Data Source or Data Target, provides a table describing the types of data being mapped between Nautobot and the other system, and, at the bottom of the page, lists the history of data synchronization involving this system.

### Executing a data sync

To synchronize data between Nautobot and a given Data Source or Data Target, select the **Sync** button for the desired integration from either the Dashboard view or the detailed view. This will bring up a form similar to that of executing any other Nautobot Job.

![Job submission form](../images/run_job.png)

Enter any appropriate parameters here, including selecting whether to execute the synchronization as a "dry run" (identifying data to be synchronized, but not actually making any changes to the system) or as an actual database update, and select **Run Job**.

You will be redirected to a standard Nautobot "Job Result" view, which will update as the Job is enqueued, begins execution, and eventually completes. When execution is complete, an **SSoT Sync Details** button will appear at the top right of the page; you can select this button for a more detailed view of the outcome.

![Job Result view](../images/job_result.png)

### Viewing a data sync record

The detailed view of a single data synchronization attempt between Nautobot and a Data Source/Target can be accessed from the Job Result view as described in the previous section, or by navigating to **Plugins > Single Source of Truth > History** and selecting the desired record from the table presented in that view.

![Sync detail view](../images/sync_detail.png)

This view describes in detail everything that occurred during the data synchronization attempt. The primary **Data Sync** tab summarizes the overall outcome of the sync attempt, including a view of the diffs (if any) identified by DiffSync and a summary of the actions taken (create, update, delete) and their outcomes (success, failure, error).

The **Job Logs** tab shows any general status messages generated by the data synchronization Job as it executed; this is equivalent to the Nautobot "Job Result" view.

The **Sync Logs** tab shows the logs captured from DiffSync regarding the individual data records being synchronized, details of any contents or changes of these records, and other detailed information. Sync logs can also be accessed directly via the **Plugins > Single Source of Truth > Logs** menu item if desired.

![Sync logs view](../images/sync_logs.png)

## Screenshots

Here is a consolidated view of all the pages within the SSoT plugin.

---

Initial dashboard showing the data targets, data sources and the last 10 syncs.
![Initial Dashboard](../images/dashboard_initial.png)

---

The detail page of the example data source.
![Example Data Source Detail](../images/data_source_detail.png)

---

The detailed page of the ServiceNow Data Target.
![ServiceNow Data Target Detail](../images/example_servicenow.png)

---

The job form page shown prior to running a job. The fields shown here depend on the job developed.
![Job Form](../images/run_job.png)

---

The job result page of running a sync.
![Example Sync Result](../images/job_result.png)

---

The sync detail page for a given sync.
![Sync Detail](../images/sync_detail.png)

---

The sync logs page for a given sync.
![Sync Logs](../images/sync_logs.png)
