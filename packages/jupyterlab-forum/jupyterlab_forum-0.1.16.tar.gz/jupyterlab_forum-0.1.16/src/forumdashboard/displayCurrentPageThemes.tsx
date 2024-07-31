export function displayCurrentPageThemes(widget:any, currentPage: number, themesPerPage: number, showThemes: any[]) {
    const themesContainer = widget.node.querySelector('#themes-container');
    if (!themesContainer) return;

    const start = (currentPage - 1) * themesPerPage;
    const end = start + themesPerPage;
    const currentThemes = showThemes.slice(start, end);

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
