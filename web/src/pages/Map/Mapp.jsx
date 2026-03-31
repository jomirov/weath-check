import './Mapp.css'

function Map() {
    return(
        <>
            <div className="map-block">
                <iframe height="90%" width="80%" style={{ borderRadius: "10px" }} src="https://embed.windy.com/embed2.html?lat=43.25&lon=76.95&zoom=6&overlay=wind"></iframe>
            </div>
            <style>
                {`
                    @media(max-width: 1280px){
                        .section--content {
                            height: 100%
                        }
                    }
                `}  
            </style>
        </>
    );
}

export default Map;