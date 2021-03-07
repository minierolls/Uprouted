<!-- routify:options preload="proximity" -->
<script>
  import { goto } from '@roxi/routify';
</script>

{#if sessionStorage.getItem('user')}
  <slot />
{:else}
  {$goto('/login')}
{/if}

