import { useEffect, useState } from 'react'
import './Home.css'


function Home( { forecastMode } ) {
    const [ loading, setLoading ] = useState(true);
    const [ currentWeatherData, setCurrentWeatherData ] = useState(null);
    const [ forecastWeatherData, setForecastWeatherData ] = useState(null);
    

    useEffect(() => {
        async function fetchData() {
            try {
                const params = new URLSearchParams(window.location.search);
                const searchingCity = params.get("city")
                const res = await fetch(`http://127.0.0.1:5000/?city=${searchingCity}`);
                const data = await res.json();
                setCurrentWeatherData(data.current_weather_data);
                setForecastWeatherData(data.forecast_weather_data);
            } catch (err) {
                console.log(err)
            } finally {
                setLoading(false)
            }
        }
        fetchData()
    }, [])

    if (loading) {
        return <div style={{ height: '500px' }}>Loading</div>
    }

    return (
        <>
            <div className="block-cards">
                <div className="block-cards--card primary-block" style={{ backgroundImage: `url("/${currentWeatherData.primary.weather_background}")` }}>
                    <div className="primary-block--group">
                        <img className="primary-block--group--weather-icon" src={`${currentWeatherData.primary.weather_icon}`} alt="w-icon"/>
                        <div className="primary-block--group--temp-block">
                            <p className="primary-block--group--temp-block--temp">{ currentWeatherData.primary.temp }°C</p>
                            <p className="primary-block--group--temp-block--night-temp">/ ночью { currentWeatherData.primary.night_temp }°C</p>
                        </div>
                    </div>
                    <p className="primary-block--date">{ currentWeatherData.primary.date }</p>
                    <p className="primary-block--city">г. { currentWeatherData.primary.city }</p>
                </div>
                <div className="block-cards--card forecast-block">
                    <div className="forecast-block--weather-icon-block" id="forecast-block--weather-icon-block">
                        { forecastMode ?
                            forecastWeatherData.forecast_for_one_day.map((record) => (
                                <img src={`${record.weather_icon}`} alt="w-icon" className="forecast-block--weather-icon-block--weather-icon"/>
                            ))
                            :
                            forecastWeatherData.forecast_for_five_days.map((record) => (
                                <img src={`${record.weather_icon}`} alt="w-icon" className="forecast-block--weather-icon-block--weather-icon"/>
                            )) 
                        }
                    </div>
                    <div className="forecast-block--temp-block" id="forecast-block--temp-block">
                        { forecastMode ? 
                            forecastWeatherData.forecast_for_one_day.map((record) => (
                                <p className="forecast-block--temp-block--temp">{ record.temp }°C</p>
                            ))
                            :
                            forecastWeatherData.forecast_for_five_days.map((record) => (
                                <p className="forecast-block--temp-block--temp">{ record.temp }°C</p>
                            ))
                        }
                    </div>
                    <div className="forecast-block--pointed-line">
                        <svg className="pointed-line" width="410" height="20">
                            <line x1="10" y1="10" x2="400" y2="10" stroke="grey" strokeWidth="2"/>
                            <circle cx="3%" cy="10" r="7" style={{fill: 'var(--blue)'}}/>
                            <circle cx="25%" cy="10" r="5" fill="grey"/>
                            <circle cx="50%" cy="10" r="5" fill="grey"/>
                            <circle cx="75%" cy="10" r="5" fill="grey"/>
                            <circle cx="98%" cy="10" r="5" fill="grey"/>
                        </svg>
                    </div>
                    <div className="srforecast-block--datetime-block" id="forecast-block--datetime-block">
                        { forecastMode ? 
                            forecastWeatherData.forecast_for_one_day.map((record) => (
                                <p className="forecast-block--datetime-block--datetime">{ record.time }</p>
                            ))
                            :
                            forecastWeatherData.forecast_for_five_days.map((record) => (
                                <p className="forecast-block--datetime-block--datetime">{ record.time }</p>
                            ))
                        }
                    </div>
                </div>
                <div className="block-cards--card secondary-block">
                    <div className="secondary-block--data-block"><p className="secondary-block--data-block--title">Температура</p><div className="isle"></div><p className="secondary-block--data-block--data">{ currentWeatherData.secondary.feels_like }°C</p></div>
                    <div className="secondary-block--data-block"><p className="secondary-block--data-block--title">Облачность</p><div className="isle"></div><p className="secondary-block--data-block--data">{ currentWeatherData.secondary.cloudiness }%</p></div>
                    <div className="secondary-block--data-block"><p className="secondary-block--data-block--title">Влажность</p><div className="isle"></div><p className="secondary-block--data-block--data">{ currentWeatherData.secondary.humidity }%</p></div>
                    <div className="secondary-block--data-block"><p className="secondary-block--data-block--title">Давление</p><div className="isle"></div><p className="secondary-block--data-block--data">{ currentWeatherData.secondary.pressure } мм. рт. ст.</p></div>
                    <div className="secondary-block--data-block"><p className="secondary-block--data-block--title">Скорость ветра</p><div className="isle"></div><p className="secondary-block--data-block--data">{ currentWeatherData.secondary.wind_speed } м/с</p></div>
                    <div className="secondary-block--data-block"><p className="secondary-block--data-block--title">Направление ветра</p><div className="isle"></div><p className="secondary-block--data-block--data">{ currentWeatherData.secondary.wind_direction }</p></div>
                </div>
                <div className="block-cards--card additional-block">
                    <div className="additional-block--data-block">
                        <div className="additional-block--data-block--div">
                            <img src="sunrise_icon.png" className="additional-block--data-block--div--sun-icon" alt="sunrise"/>
                            <p>{ currentWeatherData.secondary.sunrise }</p>
                        </div>
                        <div className="additional-block--data-block--div">
                            <img src="sunset_icon.png" className="additional-block--data-block--div--sun-icon" alt="sunset"/>
                            <p>{ currentWeatherData.secondary.sunset }</p>
                        </div>
                    </div>
                </div>
            </div>
        </> 
    )
}


export default Home;