<script context="module">

	export async function preload(page, session) {
        let { user,ux } = session;
        if (!user || ux===undefined) {
            return this.redirect(302, '/login');
        }

        return this.redirect(302, `/profile/${ux}`);
    }
</script>
