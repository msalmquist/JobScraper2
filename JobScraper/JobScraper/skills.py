# skill module
multiwordSkillList =  [ "full stack",
                        "Web Developer",
                        "Web Applications Developer",
                        "Web Engineer",
                        "Web Programmer",
                        "Web Architect",
                        "UI Developer",
                        "User Interface",
                        "Interface Developer",
                        "no sql",
                        "front end",
                        "back end",
                        "sql server",
                        "web service",
                        "object orientation",
                        "power shell",
                        "Client Server",
                        "command line",
                        "Open Source",
                        "Configuration Management",
                        "revision control",
                        "continuous integration",
                        "Data Analytics",
                        "Client Server",
                        "Test Driven Design",
                        "sql server",
                        "web site design",
                        "user experience",
                        "front end",
                        "back end",
                        "Web Page Design",
                        "desktop development",
                        "distributed development",
                        "technical writing",
                        "technical document"]

skillList = [   "Full-stack",
                "fullstack",
                "JavaScript",
                "devops",
                "CSS",
                "HTML",
                "json",
                "XML",
                "soap",
                "jsil",
                "jQuery",
                "Java",
                "R",
                "SPSS",
                "statistical",
                "Python",
                "jQuery",
                "UX",
                "UI",
                "AJAX",
                "PHP",
                "html5",
                "css",
                "css3",
                "ruby",
                "s-plus",
                "testing",
                "nosql",
                "xml",
                "c#",
                "Photoshop",
                "sql server",
                "mysql",
                "c++",
                "Oracle",
                "Perl",
                "iOS",
                "iPhone",
                "Linux",
                "Java",
                "Javascript",
                "Apple",
                "android",
                "XAML",
                "Xamarin",
                "PHP",
                "UI",
                "UX",
                "Matlab",
                "OOP",
                "powershell",
                "databases",
                "git",
                "svn",
                "API",
                "deployment",
                "Installshield",
                "CI",
                "Diagnostics",
                "subversion",
                "TDD",
                "BDD",
                "Analytics",
                "GIS",
                "ESRI",
                "mysql",
                "agile",
                "architecture",
                "analytics",
                "api",
                "debugging",
                "photoshop",
                "git",
                "svn",
                "subversion",
                "github",
                "ruby",
                "front end",
                "Perl",
                "PHP",
                "frontend",
                "backend",
                ".net",
                "MVC",
                "Angular.js",
                "Angular",
                "CoffeeScript",
                "XML",
                "HTML",
                "C++",
                "mobile",
                "remote",
                "distributed",
                "documentation"]

skillsDict = dict()

def InitSkillsDict():
    global skillsDict
    skillsDict.clear
    for mwskill in multiwordSkillList:
            temp = str.lower(mwskill)
            skillsDict[temp] = 0
    for skill in skillList:
        temp = str.lower(skill)
        skillsDict[temp] = 0

def ProcessTextBlock(txtBlk):
    global skillsDict
    foundCnt = 0
    if len(skillsDict) == 0:
        InitSkillsDict()
    lc_txt = str.lower(txtBlk)
    for key, value in skillsDict.items():
        ind = str.find(lc_txt, key)
        if ind > -1:
            skillsDict[key] = value + 1
            foundCnt = foundCnt + 1
            # get rid of the multiword string so that
            # words in it are not counted twice
            if str.find(' ', key) > -1:
                str.replace(lc_txt, key)
    print("Found: ", str(foundCnt))

def PrintResults():
    global skillsDict
    for key, value in skillsDict.items():
        if value != 0:
            print (key, ", Count: ", value)