<script context="module">

	export async function preload(page, session) {
        let { user,ux } = session;
        if ( !user ) {
            return this.redirect(302, '/login');
        }
        if(ux===undefined) return this.redirect(302, '/login');
        return this.redirect(302, `/profile/${ux}`);
    }
</script>
Loading...