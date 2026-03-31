import './Home.css'

function PostHeaderForSearch( { setForecastMode } ) {

    function searchCity (e) {
        e.preventDefault();
        const params = new URLSearchParams(window.location.search);
        const search_input = document.getElementById("search-block--input--city-search");
        params.set("city", search_input.value);
        window.location.search = params.toString();
    }

    function changeForecastMode(event) {
        if (event.target.checked == true) {
            setForecastMode(false);
        } else {
            setForecastMode(true);
        }
    }

    return (
        <>
            <form className="search-block" id="search-block" onSubmit={ searchCity }>
                <input id="search-block--input--city-search" type="text" placeholder="Введите город"/>
                <button className="search-block--btn" id="search-block--btn" type="submit">
                    <svg className="search-block--search-svg" width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M3.2218 3.22182C7.51757 -1.07394 14.4827 -1.07394 18.7784 3.22182C23.0739 7.51761 23.0741 14.4828 18.7784 18.7785C14.4828 23.0741 7.51759 23.0739 3.2218 18.7785C-1.07397 14.4827 -1.07397 7.51759 3.2218 3.22182ZM16.6564 5.34292C13.5322 2.21894 8.46702 2.2188 5.3429 5.34292C2.21879 8.46704 2.21892 13.5322 5.3429 16.6564C8.46708 19.7806 13.5322 19.7806 16.6564 16.6564C19.7806 13.5322 19.7806 8.46711 16.6564 5.34292Z" fill="#545454"/>
                        <rect x="24.4348" y="27.2633" width="13" height="4" rx="2" transform="rotate(-135 24.4348 27.2633)" fill="#545454"/>
                    </svg>
                </button>
            </form>
            <label className="forecast-mode-changer-label">
                <input className="forecast-mode-changer-label--checkbox" id="forecast-mode-changer-label--checkbox" onChange={(event) => changeForecastMode(event)} type="checkbox"/>
                <span className="forecast-mode-changer-label--span">Дневной</span>
            </label>
        </>
    )
}
export default PostHeaderForSearch;