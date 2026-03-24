import { Outlet } from "react-router-dom"

function PostHeaderLayout() {
    return (
        <>
            <div className="post-header">
                <div className="post-header--block-div">
                    <Outlet/>
                </div>
            </div>
        </>
    )
}
export default PostHeaderLayout