import { Widget } from '@lumino/widgets';
import { ShowThemeDetail } from './showthemedetail';
import { handleCreateThemeClick } from './CreateTheme';


export class ForumDashboardWidget extends Widget {

    private originalHTML: string; // Declare the property
    private activeTab: string = 'all'; // Track the active tab
    private currentPage: number = 1; // Track the current page
    private themesPerPage: number = 5; // Maximum number of themes per page
    private allThemes: any[] = []; // Store all themes
    private showThemes: any[] = []; // Store all themes

    constructor(private username: string, private forumEndpointUrl: string) {
        super();
        this.addClass('forumWidget');
        this.originalHTML = `
            <header>
                <!--NavBar Section-->
                <div class = "navbar">
                    <div class="forum-title">Databrix Lab Forum</div>
                </div>
            </header>
            <div class="container">
              <div class="tabs">
                <button class="tab" data-tab="all">All</button>
                <button class="tab" data-tab="open">Open</button>
                <button class="tab" data-tab="closed">Closed</button>
              </div>
              <button class="create-theme-button" id="createThemeButton">Create Theme</button>
            </div>
              <div class="subforum">
                <div class="subforum-title">
                  <h1>General Information</h1>
                </div>
                <div id="themes-container"></div>
                <div id="pagination-controls" class="pagination-controls"></div>
              </div>
            </div>
            `;
        this.node.innerHTML = this.originalHTML; // Set initial HTML
        this.fetchAndDisplayThemes();

        // Event listener
        this.node.addEventListener('click', (event) => {
            const target = event.target as HTMLElement; // Get the clicked element

            if (target.classList.contains('create-theme-button')) {
              handleCreateThemeClick(this, this.username, this.forumEndpointUrl);
            }

            if (target.classList.contains('tab')) {
              this.activeTab = target.dataset.tab ?? 'Open'; // Default to 'all' if undefined
              this.currentPage = 1
              this.updateTabDisplay();
            }

            if (target.classList.contains('description-link')) { // Check if it's the correct link
                const ThemeID = target.getAttribute('data-description-id');
                event.preventDefault(); // Prevent default link behavior
                ShowThemeDetail(this, ThemeID, this.forumEndpointUrl, username);
            }

            if (target.classList.contains('page-link')) { // Page navigation link
                this.currentPage = parseInt(target.dataset.page ?? '1', 10);
                this.displayCurrentPageThemes();
            }
        });
    }


    private async fetchAndDisplayThemes() {

        // Fallback example themes declared outside of try-catch block
        const exampleThemes = [
            {
              ThemeID: 1,
              Title: "Example Theme 1",
              Author: "Admin",
              CreationTime: "2024-07-01T10:00:00",
              Status: "open"
            },
            {
              ThemeID: 2,
              Title: "Example Theme 2",
              Author: "User123",
              CreationTime: "2024-07-15T15:30:00",
              Status: "closed"
            },
            {
              ThemeID: 3,
              Title: "Example Theme 2",
              Author: "User123",
              CreationTime: "2024-07-15T15:30:00",
              Status: "closed"
            },
            {
              ThemeID: 4,
              Title: "Example Theme 2",
              Author: "User123",
              CreationTime: "2024-07-15T15:30:00",
              Status: "closed"
            },
            {
              ThemeID: 5,
              Title: "Example Theme 2",
              Author: "User123",
              CreationTime: "2024-07-15T15:30:00",
              Status: "closed"
            },
            {
              ThemeID: 6,
              Title: "Example Theme 2",
              Author: "User123",
              CreationTime: "2024-07-15T15:30:00",
              Status: "closed"
            },
            {
              ThemeID: 2,
              Title: "Example Theme 2",
              Author: "User123",
              CreationTime: "2024-07-15T15:30:00",
              Status: "closed"
            },
        ];

        try {
            const response = await fetch(this.forumEndpointUrl);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            this.allThemes = data.themes;
            this.showThemes = this.allThemes
        } catch (error) {
            console.error('Error fetching themes:', error);
            this.allThemes = exampleThemes;
            this.showThemes = this.allThemes
        }

        this.displayCurrentPageThemes();
        this.updatePaginationControls();
    }

    private updateTabDisplay() {
      // Filter the themes based on their status
      this.showThemes = this.allThemes.filter(theme => {
          return this.activeTab === 'all' || theme.Status === this.activeTab;
      });

      this.displayCurrentPageThemes();
      this.updatePaginationControls();
    }


    private displayCurrentPageThemes() {
        const themesContainer = this.node.querySelector('#themes-container');
        if (!themesContainer) return;

        const start = (this.currentPage - 1) * this.themesPerPage;
        const end = start + this.themesPerPage;
        const currentThemes = this.showThemes.slice(start, end);

        themesContainer.innerHTML = currentThemes.map((theme: any) => `
            <div class="subforum-row">
                <div class="subforum-description subforum-column">
                    <h4><a href="#" class="description-link" data-description-id="${theme.ThemeID}">${theme.Title}</a></h4>
                    <p>Created by ${theme.Author} on ${new Date(theme.CreationTime).toLocaleDateString()}</p>
                    <p>Status: ${theme.Status}</p>
                </div>
                <div class="subforum-info subforum-column">
                    <b><a href="#">Posted</a></b> by <a href="#">${theme.Author}</a>
                </div>
            </div>
            <hr class="subforum-devider">
        `).join('');
    }

    private updatePaginationControls() {
        const paginationControls = this.node.querySelector('#pagination-controls');
        if (!paginationControls) return;

        const totalPages = Math.ceil(this.allThemes.length / this.themesPerPage);
        let paginationHTML = '';

        for (let i = 1; i <= totalPages; i++) {
            paginationHTML += `<button class="page-link" data-page="${i}">${i}</button>`;
        }

        paginationControls.innerHTML = paginationHTML;
    }


}
