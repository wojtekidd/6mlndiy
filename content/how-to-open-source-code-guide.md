Title: How to open source any code inside your company and what to remember about when doing so.
Date: 2021-12-08 13:33
Tags: open-source, open source, guide
Slug: how-to-open-source-code-guide
Authors: Wojtek Cichon
Summary: Here's a short breakdown of the things you have to remember about when open-sourcing code in a proffessional env.

![Open source meme]({static}/images/one-does-open-source.jpg "One does not simply open source code meme")

Being in various job recruitments related to Open Source Software and having some experience in the field I’ve bumped into the following question:

*“How would you open source a piece of software and what benefits would it give to your company?”*

This caught me off guard as I was always sure that open source is the way to go and kind of treated this way of distributing software as there were no other options (probably because I landed my first tech job at an OSS company). When trying to answer this question I couldn’t come up with a precise and elaborate answer. Only now, after open-sourcing a feature phone operating system from scratch, I can tell exactly how such a process might look like.

## Why should we open-source my codebase?

To state the obvious - Open Source has won, etc. But let’s put it in a business perspective:

1. **Sustainability and longevity** - even if your company suddenly switches to doing something completely different, goes low on manpower when it comes to sustaining its open-source code, or completely disappears from the face of the planet, there is still value in your code that can be sustained by a vibrant open source community.  

2. **Transparency** - if transparency is one of the core values inside your company or product community then open sourcing software is a living (giting?) proof that you’re serious about your values and give back to the community.

3. **Security and quality** - more eyes on the code, more bugs squashed, more discussions about how to do things properly and securely.  
     
4. **Interoperability** - there are always people who see that your piece of code could be used in a different context or be combined with other solutions to bring more value to more people. This aspect builds on collaboration and transparency as well.

I’m leaving out the case of open source business models here since the topic is big and complex, but just remember that there are dozens of companies that earn gazillions and have their code completely open or distributed in [an open core model](https://www.wikiwand.com/en/Open-core_model).

## Where should I start? (AKA I have the code, now what?)

### Get the organization’s buy-in first

Let’s assume that you’re a newcomer to a company and your mission is to open source a piece of code that the development team has been working on for the past X years. You have to start building trust with both engineering and business units so that everyone is on the same page, knows what you’re trying to achieve and why it’s crucial to your business.

Create a simple presentation introducing every group to the idea of Open Source and your particular case enumerating the business profits of going OSS. Be ready to address the fears of specific groups. Developers mostly fear that someone from the other side of the planet might find their code too spaghetti or spark up discussions around certain decisions that are reflected inside the code.

The business units might be afraid that going open source means the end of business and profits as they know it (“Giving **OUR** code away? For **FREE**?”)

What I did is I used [this pretty good short animation to explain why open source is good](https://www.youtube.com/watch?v=a8fHgx9mE5U) inside a Google sheet presentation explaining:

- What is Open Source
- Why it has been invented
- Why it’s good for our company
- What are the next steps (for engineering and business teams alike)

Holding these meetings separately inside specific teams and talking about the open-source movement will also help you out in identifying your first “go-to” people regarding writing documentation, making decisions, contacting the community, etc.

The other way round is going to your Git platform admin and saying “Hi I’m Wojtek and I will open-source all your repos! Gimmie access!”

## Decide on an open-source license

Ask yourself these questions:

- What are the business purposes of open source code in my company (if any)?
- What are the business risks of open source code in my company (if any)?

Then read about the differences between licenses - my place to go is most often this [“Choose an open-source license” page by GitHub](https://choosealicense.com/). Easy to navigate and straightforward although…

## Beware of the third-party software licenses trap

Not really a trap tough - just wanted to add some exciting plot twist inside the article.

Basically, it’s about what kind of licensed software you already have inside the piece of the codebase you’re trying to open up for contributions.

You can have all of these: permissive, less-permissive, proprietary, etc. It can get complicated but in most cases, you have to make sure that:

1. The license you choose doesn’t null other less-permissive licenses that your code includes (especially watch out for GPL which GPLs everything it touches)

2. You have paid a license fee for any open source code that is inside your codebase (so that your codebase can be used for commercial purposes)  

3. Any proprietary assets and pieces of code are hidden to the eyes of the open-source community and are available only to the eyes of your company as the sole owner of the aforementioned. This part might mean that you’ll have to store assets in closed repos and link to them (suck them in) only when building your software for commercial purposes (make sure that you start doing so from the beginning, otherwise the links to proprietary pieces of digital assets stay in your Git history). [Remember to check your fonts licenses as well.](https://pixelambacht.nl/2017/github-font-piracy/)

This part can get complicated so don’t hesitate to reach out to people who own these codebases to make sure that you’re not infringing any licenses. After you get these details settled make sure that you describe everything inside your \`LICENSE.md\` file which is the default place to store your license info.

## Start with the documentation

### The structure of technical documentation

I’ll be brief here because it’s also a topic for separate discussions and articles. I usually stick to [this structure for docs](https://documentation.divio.com/structure/) which was an eye-opener when I first read it. Make sure that you write the README.md in such a way that a person who isn’t technical and bumps into your repository by accident can say what this piece of code does and where they can start setting it up locally and exploring it further.

### A how-to contribute article

Be precise on how to start contributing to your code, explain the development workflow and localization workflow. Make sure that your repository is set up in such a way that people outside of your organization can contribute Pull Requests from forks, have the access rights to read the outcomes (logs, errors) of your CI pipeline, and can’t merge to the main branch without a proper code review from the maintainers of the code.

### Code of conduct and inclusiveness

Nowadays a Code of Conduct is a must-have so don’t forget about one. I recommend appropriating the [CONTRIBUTOR COVENANT](https://contributor-covenant.org/) and tweaking it to your needs.

[Remember to be inclusive](https://todogroup.org/guides/diversity-inclusion/) - wording matters.

## Good first issues and issue templates

Good first issues are the issues you can tag on the issue board to signal what are the low-hanging fruits. These might be pieces of documentation, entry-level code fixes, or test fixes that can be done by anyone with some proficiency in the programming language your codebase is written in.

You can also set up some issue (and pull request) templates for your community so that whenever a new person addresses the issue you take them by the hand and help them describe it whether it’s a bug / feature request / new localization / anything else. There is [a fun way to generate issue and PR templates](https://www.talater.com/open-source-templates/) as well.

## Contributor License Agreement

Oh no, another license! Or an agreement? Or whatever this is…  

CLA is an important piece of the puzzle if you’re open-sourcing code that your company uses for commercial purposes (so I guess in most cases). This is an agreement between your contributors and your company as the code maintainer that all intellectual rights of future contributions will be ‘owned’ by the maintainer. This is a legal backup that you need to have just to make sure that when your company earns its first mill, it won’t be sued in court by someone who added a tiny functionality to the code.

Signing the CLA can be automated and I highly recommend you set up this process with the help of [this CLA assistant](https://cla-assistant.io/). You can also find some ready-made CLA texts out there just waiting for you to be (responsibly) copied and pasted.

## Get it out there!

Once you feel that your code is ready to welcome your first contributors go spread the word! Use your in-house marketing team to help you and make sure that you also share the news in all relevant tech outlets. Too many to name here.

If you’re hesitant to open the codebase for the entire world at one go, you can start with a “Developer preview” - a process where you screen all the people that want to contribute to your code by letting a small amount of them onto the repository and seeing how they react. Stay in touch with your first contributors and make sure that you attend to their needs and suggestions. Give out your product or company swag to your first contributors and make them feel welcome at the earliest stages - even if it’s a developer preview.

## Refine and repeat

Once you get your first codebase running on open source, you can simply repeat the process with other repos and flood the world with even more open-source code.



I hope that someone searching for “How and why should I open source my codebase” will find this article helpful and land their next job at helpful enough that they will use it to land a job at (insert your dream company name here) or make a clear step-by-step plan of what has to be done on their current job involving open source.

