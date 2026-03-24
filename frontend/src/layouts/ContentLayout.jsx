import { Outlet } from "react-router-dom";

function ContentLayout() {
    return (
        <>
            <section className="section--content">
                <Outlet/>
            </section>
            <style>
                {`
                    .section--content {
                        display: flex;
                        height: 100%;
                        width: 100%;
                        background-color: #eaeaea;
                    }
                `}
            </style>
        </>
    )
}
export default ContentLayout;