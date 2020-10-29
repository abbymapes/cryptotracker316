<script>
    import { stores } from "@sapper/app";
    const { page,session} = stores()

    const { slug } = $page.params;
</script>



{slug}
