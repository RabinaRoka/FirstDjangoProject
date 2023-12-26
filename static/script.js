console.log("script running...asassas")
console.log("hello")
document.querySelector('.cross').style.display ='none'; //for not showing cross button
document.querySelector('.hamburger').addEventListener("click", () =>{  //While clicking hamburger icon
    document.querySelector('.sidebar').classList.toggle('sidebarGo'); //for showing sidebar we use toggle
    if(document.querySelector('.sidebar').classList.contains('sidebarGo')){
        document.querySelector('.ham').style.display ='inline'  //for showing ham
        document.querySelector('.cross').style.display ='none' //for not showing ham

    }else{
        document.querySelector('.ham').style.display ='none'  //for not showing ham
        setTimeout(() => {

        document.querySelector('.cross').style.display ='inline'},10); 
          //for showing ham
       
    }
})

// document.getElementById("learn-more-button").addEventListener("click", function() {  //redirect to blog page
//     window.open("https://rabina610795847.wordpress.com/", "_blank");   //opening link in another page
// });

  // Get all elements with the class "learn-more-button"
  const learnMoreButtons = document.querySelectorAll(".learn-more-button");

  // Loop through each button and attach a click event listener
  learnMoreButtons.forEach(button => {
      button.addEventListener("click", function() {
          // Get the link from the data-link attribute of the clicked button
          const link = button.getAttribute("data-link");
          
          // Open the link in a new tab
          window.open(link, "_blank");
      });
  });

  const projects = [
    {
      title: "Web Design - Investina",
      image: "Investina.jpg",
      description: `At the present time, many peoples are interested in investing but usually lack the knowledge related to 
      investing platform. Additionally, after investing in different field individuals have their excel sheet file and 
      they wants to convert their investment portfolio data from CSV or Excel files into visually appealing graphs 
      or pie charts, making it easier to explain their investment portfolio to others, particularly their parents. So, to 
      overcome this problem, I have decided to developed web application named “Investina” focusing on 
      providing educational resources related to investments. The website provides users with up-to-date 
      information on the stock market, Investment calculator, age category budget etc.
      By designing this web application, I hope to solve above problem and deliver new investors with the 
      information and resources they need to effectively navigate the world of investing. It offerstools for managing 
      and visualizing investment portfolios. With interactive elements, step-by-step instructions, and simple 
      descriptions to make learning and understanding easier, the scheme is designed to meet the needs of initial 
      investors. The product creator should ensure that the needs and limitations of the users are taken into account 
      when creating these features so that users can benefit from them.<br>
      You can click here for viewing the prototype of design.`,
      link: "https://www.figma.com/file/rdf3ONy65UvnUXnA2mqCZO/2204959__task-2_Prototype?type=design&node-id=0-1&mode=design",
    },
    {
      title: "Project 2",
      image: "IMG.png",
      description: ``,
      link: "project2.html",
    },
    // Add more projects...
  ];
  
  // Function to generate project items
  function generateProjectItem(project) {
    const projectItem = document.createElement("div");
    projectItem.classList.add("project");
    
    const image = document.createElement("img");
    image.src = `/static/${project.image}`    //image should be inside static folder and we should write static
    projectItem.appendChild(image);
  
    const title = document.createElement("h2");
    title.textContent = project.title;
    projectItem.appendChild(title);
  
    const desc = document.createElement("p");
    desc.textContent = project.description;
    projectItem.appendChild(desc);
  
    const link = document.createElement("a");
    link.href = project.link;
    link.textContent = "Learn More";
    projectItem.appendChild(link);
  
    return projectItem;
  }
  
  // Add project items to the projects grid
  const projectsGrid = document.getElementById("projects-grid");
  projects.forEach(project => {
    const projectItem = generateProjectItem(project);
    projectsGrid.appendChild(projectItem);
  });