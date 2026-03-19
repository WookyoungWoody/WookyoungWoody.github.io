// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "Peer-reviewed journal papers and conference proceedings in thermal-fluid engineering.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Research projects in thermal-fluid engineering and software development.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "GitHub repositories and open-source contributions.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Curriculum Vitae of Wookyoung Kim, Ph.D. — Senior Researcher at KIMM.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-welcome-to-my-academic-portfolio-this-site-showcases-my-research-in-thermal-fluid-engineering-at-kimm",
          title: 'Welcome to my academic portfolio! This site showcases my research in thermal-fluid engineering...',
          description: "",
          section: "News",},{id: "projects-data-center-cooling",
          title: 'Data Center Cooling',
          description: "Immersion cooling and direct liquid cooling for next-generation high-heat-density servers",
          section: "Projects",handler: () => {
              window.location.href = "/projects/datacenter_cooling/";
            },},{id: "projects-heat-pump-systems",
          title: 'Heat Pump Systems',
          description: "Chemisorption, adsorption, and high-temperature heat pump research",
          section: "Projects",handler: () => {
              window.location.href = "/projects/heatpump/";
            },},{id: "projects-pche-for-liquid-hydrogen",
          title: 'PCHE for Liquid Hydrogen',
          description: "Printed Circuit Heat Exchanger design and testing for cryogenic applications",
          section: "Projects",handler: () => {
              window.location.href = "/projects/pche/";
            },},{id: "projects-engineering-software",
          title: 'Engineering Software',
          description: "Thermal performance prediction tools and cross-platform apps",
          section: "Projects",handler: () => {
              window.location.href = "/projects/software/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%77%6F%6F%6B%79%6F%75%6E%67@%6B%69%6D%6D.%72%65.%6B%72", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/WookyoungWoody", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=qhSKdD8AAAAJ", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0009-0000-8038-7619", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/wookyoungwoody", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
