eadhost
=======

static site generator and free hosting service for [encoded archival description](http://www.loc.gov/ead/)

Goals
-----

Create an open source free hosting service for Encoded Archival Description that allows archival arrangement 
and description projects to effortlessly publish finding aids on the web by registering a GitHub repository 
(of CC0 licensed?) EAD files.  

Once registered, static HTML (and PDF?) versions will be created and hosted free of charge to contributing repositories.
The published versions will be automatically regenerated when changes in encoded description is pushed to 
github.


### Search

No cross colleciton searching will be provided by the static hosting service.  It is expected that users
will search with Google and OCLC Research's [ArchiveGrid](http://beta.worldcat.org/archivegrid/). 

### Related digital objects and information resources
No object hosting will be provided (except for maybe generated PDF files), but links to objects and related resources
that are explicitly encoded or otherwise discoverable will be supported.

### EAD version support
The goal is to support any valid EAD2002XSD, EAD2002DTD, or EAD3 xml instance.

### Use of Google Analytics
It would be easy to track all the pages using google analytics and allow contributors to also add thier google analytics tracker to their pages.


Parts
-----

### Software
 * python flask server to take pings from github and add to SQS queue (runs on master)
 * python script to run periodically to make sure workers are running if there are items in the SQS queue. If there is work to do but no/not enough workers, it will make spot market bid for a new worker. (runs on master)
 * website that uses github's OAuth where contributors can register github repositories
 * ansible playbooks for workers and master
 * python script to check the SQS queue for work, run maven, updates index pages, and then terminate if no work for x. (runs on worker)
 * maven pom.xml that runs saxon and git commands (runs on worker)
 * XSLT to convert EAD to HTML (runs on worker)
 * PDF generation (special pdfworker) {phase two if demand}

### Servers
 * master will be a t1.micro high utilization reserved EC2 instance running 24/7
 * worker will be a spot EC2 instance running as needed
 * webworker
 * pdfworker
 * generated files will be stored in an S3 bucket and served up with CloudFront / or use github pages for hosting generated files?

### Configuration
Some sort of `.repo-info.yml` will need to be set up that will contain up-to-date repository contact information and 
the current prefered repository label and other configuration information.

Open Company
------------

> 1. **Be as open as possible.** An open company develops all of its products publicly, and freely shares all of its intellectual property. Any software it writes is open source. It publishes as much financial and other data as it can without compromising customer privacy. All employees of the company are publicly listed along with their level of access to private company information and private customer data.
> 2. **Charge as little as possible.** An open company tries to charge as little for its products and services as possible. Price to cost, that is, instead of to value.
> 3. **Don’t compensate employees.** Employees of an open company don’t earn a wage or salary or receive benefits from the company. Their only distinction from non-employees is their access to sensitive data, such as private customer data, passwords, and detailed financial information.

from [The Gittip Blog: THE FIRST OPEN COMPANY](http://blog.gittip.com/post/26350459746/the-first-open-company)

Funding
-------
Expenses for hosting will be paid by Brian Tingle with personal funds for the time being, but a crowd funding option 
such as [Gittip](https://www.gittip.com) may be explored in the future.


Please Help
-----------
Any feedback, suggestions, pull requests welcome.

