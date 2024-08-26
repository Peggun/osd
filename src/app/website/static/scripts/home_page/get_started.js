const sections = ['#features', '#news', '#buttons']; // Add more sections as needed
const tooltips = [
  'Explore the key features of OSD and what they do.', 
  'Stay updated with the latest news and releases.', 
  'Navigate to different sections of the site.'
]; // Text for each section
let currentSection = 0;

function start_get_started() {
  // Show the overlay
  document.querySelector('.overlay').style.display = 'block';
  scrollToSection(currentSection);

  // Add the "Next" button to the bottom left corner
  const button = document.createElement('button');
  button.classList.add('bottom-left-button');
  button.textContent = 'Next';
  button.onclick = () => {
    currentSection++;
    if (currentSection < sections.length) {
      scrollToSection(currentSection);
    } else {
      endTour();
    }
  };
  document.body.appendChild(button);
}

function scrollToSection(sectionIndex) {
  const section = document.querySelector(sections[sectionIndex]);
  const rect = section.getBoundingClientRect();
  window.scrollTo({
    top: window.pageYOffset + rect.top - 100, // Adjust as needed
    behavior: 'smooth'
  });

  highlightSection(section);
  showTooltip(section, tooltips[sectionIndex]);
}

function highlightSection(section) {
  // Remove the highlight from any previous section
  document.querySelectorAll('.highlighted').forEach(el => el.classList.remove('highlighted'));

  // Highlight the current section
  section.classList.add('highlighted');
}

function showTooltip(section, text) {
  let tooltip = document.querySelector('.tooltip');
  
  // Create tooltip if it doesn't exist
  if (!tooltip) {
    tooltip = document.createElement('div');
    tooltip.classList.add('tooltip');
    document.body.appendChild(tooltip);
  }
  
  tooltip.textContent = text;
  const rect = section.getBoundingClientRect();

  // Position the tooltip near the section
  tooltip.style.top = `${window.scrollY + rect.top - tooltip.offsetHeight - 10}px`;
  tooltip.style.left = `${rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2)}px`;

  // Show the tooltip
  tooltip.style.display = 'block';
}

function endTour() {
  // Hide the overlay and tooltip
  document.querySelector('.overlay').style.display = 'none';
  document.querySelector('.tooltip').style.display = 'none';

  document.querySelector('.highlighted').classList.remove('highlighted');
  
  // Remove the "Next" button
  document.querySelector('.bottom-left-button').remove();

  window.location.replace('home')
}
