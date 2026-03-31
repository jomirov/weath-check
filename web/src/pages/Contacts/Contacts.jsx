import "./Contacts.css"

export default function Contacts() {
    return (
        <>
            <div className="contacts-block">
                <div className="contacts-block--div">
                    <div className="contacts-block--div--contacts" style={{height: "max-content"}}>
                        <h1>Контакты</h1>
                        <p style={{marginTop: "30px" }}>Email: example123@gmail.com</p>
                        <p>Facebook: www.facebook/id2312424.com</p>
                        <p>Telegram/Whatsapp: +7 707 777 77 77</p>
                    </div>
                    <img style={{ width: "55%" }} src="./weath_check.svg"/>
                </div>
            </div>
        </>
    );
}