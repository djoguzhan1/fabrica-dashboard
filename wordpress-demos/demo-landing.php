<?php
/**
 * Plugin Name: Demo Landing Pages
 * Description: Serves the CoolAir HVAC and ProFix Plumbing landing pages as WordPress pages with a full-width template.
 */

const DEMO_LANDING_ASSETS = 'https://djoguzhan1.github.io/web-dev-portfolio/demos/';

function demo_landing_slug() {
	if ( ! is_singular( 'page' ) ) {
		return '';
	}
	return (string) get_post_meta( get_queried_object_id(), '_demo_landing', true );
}

add_filter( 'template_include', function ( $template ) {
	return demo_landing_slug() ? __DIR__ . '/demo-landing/template.php' : $template;
} );

add_action( 'wp_enqueue_scripts', function () {
	$slug = demo_landing_slug();
	if ( ! $slug ) {
		return;
	}
	// The block theme's global styles and block CSS would override the landing page's own design system.
	foreach ( array( 'global-styles', 'wp-block-library', 'wp-block-library-theme', 'classic-theme-styles', 'core-block-supports' ) as $handle ) {
		wp_dequeue_style( $handle );
	}
	wp_enqueue_style( 'demo-landing', DEMO_LANDING_ASSETS . $slug . '/styles.css', array(), null );
	wp_enqueue_script( 'demo-landing', DEMO_LANDING_ASSETS . $slug . '/main.js', array(), null, array( 'strategy' => 'defer', 'in_footer' => true ) );
}, 100 );

add_filter( 'show_admin_bar', function ( $show ) {
	return demo_landing_slug() ? false : $show;
} );
